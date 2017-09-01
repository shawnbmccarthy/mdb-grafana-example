var mongoUtil = require('../utils/mdb_util');

module.exports = {
    generateDims: function(collectionName, dim, callback){
        var db   = mongoUtil.getDb();
        var coll = db.collection(collectionName);
        coll.distinct('val.dim.' + dim, function(err, doc){
            if(err){
                callback(err, null);
            } else {
                callback(null, doc);
            }
        });
    },
    generateDataPoints: function(collectionName, dim, params, callback){
        var db      = mongoUtil.getDb();
        var coll    = db.collection(collectionName);
        var from    = new Date(params.range.from);
        var to      = new Date(params.range.to);
        var limit   = params.maxDataPoints;
        var targets = params.targets;
        var search  = {$or: []};

        console.log(params);
        /*
         * grafano passes targets as an array of objects for each element
         * these elements can be of type timeserie or table, currently
         * all table variables are ignored
         * TODO: add support for tables
         */
        for(var i = 0; i < targets.length; i++){
            if(targets[i].type === 'timeserie'){
                search.$or.push({$eq: ['$$val.dim.' + dim, targets[i].target]});
            }
        }

        /*
         * TODO: Can we improve this
         * TODO: create index on date (definitely) and rep, maybe?
         * TODO: manage cursors
         */
        coll.aggregate([
            {$match: {date: {$gte: from, $lte: to}}},
            {$project:{_id: 0, date: 1, val:{$filter:{input: '$val', as: 'val', cond: search}}}},
            {$unwind: '$val'},
            {$project: {date: 1, dim: '$val.dim.' + dim, value: '$val.value'}},
            {$group: {_id: {date: '$date', dim: '$dim'}, avgValue: {$avg: '$value'}}},
            {$project: {date: '$_id.date', dim: '$_id.dim', avgValue: '$avgValue', _id: 0}},
            {$group: {_id: '$dim', results: {$addToSet: {avgValue: '$avgValue', date: '$date'}}}},
            {$project: {target: '$_id', datapoints: '$results', _id: 0}},
            {$limit: limit}
        ], function(err, results){
            if(err){
                callback(err, null);
            } else {
                var returns = [];
                for (var i = 0; i < results.length; i++) {
                    var datapoints = results[i].datapoints;
                    datapoints = datapoints.sort(function (a, b) {
                        return new Date(a.date).getTime() - new Date(b.date).getTime()
                    });
                    var dps = [];
                    for (var j = 0; j < datapoints.length; j++) {
                        d = [];
                        d.push(datapoints[j].avgValue);
                        d.push(datapoints[j].date.getTime());
                        dps.push(d);
                    }
                    returns.push({target: results[i].target, datapoints: dps});
                }
                callback(null, returns);
            }
        });
    }
};