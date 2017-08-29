/*
 * route for grafana minutes datasource
 * {
 *	"_id" : ObjectId("59259c26374f5c213002d1da"),
 *	"_class" : "com.mongodb.BasicDBObject",
 *	"userId" : "zywave",
 *	"date" : ISODate("2017-05-24T04:00:00Z"),
 *	"mm" : 4,
 *	"val" : [
 *		{
 *			"dim" : {
 *				"rep" : "M3C",
 *				"dob_yr" : "1986",
 *				"acct_type" : "*",
 *				"state" : "*"
 *			},
 *			"value" : 50184.38
 *		},
 *	....
 *	]
 * }
 *
 * How do we want to display the data
 */
var express   = require('express');
var mongoUtil = require('../utils/mdb_util');
var router    = express.Router();

router.post('/', function(req, res) {
  console.log(req.body);
  res.json({results: 'success'});
  res.end();
});

/*
 * search is called when building the metrics - currently we will focus on
 * timeseries for the minute data - avg value across the various reps
 */
router.post('/search', function(req, res){
  var db = mongoUtil.getDb();
  var coll = db.collection('minutes');
  coll.aggregate([
      {$unwind: '$val'},
      {$project: {_id: 0, rep: '$val.dim.rep'}},
      {$group: {_id: 'rep', targets: {$addToSet: '$rep'}}},
      {$project: {_id: 0}},
      {$limit: 1}
  ], function(err, results){
    if(err){
      res.json([]);
      res.sendStatus(500);
    } else {
        console.log(results);
        res.json(results[0]['targets'].sort());
        res.end();
    }
  });
});

/*
 * what will be some key annotations?
 */
router.post('/annotations', function(req, res) {
  results = [];
  res.json([]);
  res.end();
});

/*
 * don't support tables yet
 */
router.post('/query', function(req, res){
  var from    = new Date(req.body.range.from);
  var to      = new Date(req.body.range.to);
  var limit   = req.body.maxDataPoints;
  var db      = mongoUtil.getDb();
  var coll    = db.collection('minutes');
  var targets = req.body.targets;
  var search  = [];

  console.log(req.body);
  for(var i = 0; i < targets.length; i++){
      if(targets[i].type === 'timeserie'){
          search.push(targets[i].target);
      }
  }

  coll.aggregate([
      {$match: {date: {$gte: from, $lte: to}}},
      {$unwind: '$val'},
      {$match: {'val.dim.rep': {$in: search}}},
      {$project: {_id: 0, date: 1, rep: '$val.dim.rep', value: '$val.value'}},
      {$group: {_id: {date: '$date', rep: '$rep'}, avgValue: {$avg: '$value'}}},
      {$project: {date: '$_id.date', rep: '$_id.rep', avgValue: '$avgValue', _id: 0}},
      {$group: {_id: '$rep', results: {$addToSet: {date: '$date', avgValue: '$avgValue'}}}},
      {$project: {target: '$_id', datapoints: '$results', _id: 0}},
      {$limit: limit}
  ], function(err, results){
      if(err){
          res.json([]);
          res.sendStatus(500);
      } else {
          var returns = [];
          for(var i = 0; i < results.length; i++){
              var datapoints = results[i].datapoints;
              datapoints = datapoints.sort(function(a,b){return new Date(a.date).getTime() - new Date(b.date).getTime()});
              var dps = [];
              for(var j = 0; j < datapoints.length; j++){
                  d = [];
                  d.push(datapoints[j].avgValue);
                  d.push(datapoints[j].date.getTime());
                  dps.push(d);
              }
              returns.push({target: results[i].target, datapoints: dps});
          }
          console.log('here');
          console.log('%j', returns);
          res.json(returns);
          res.end();
      }
  });
});

module.exports = router;