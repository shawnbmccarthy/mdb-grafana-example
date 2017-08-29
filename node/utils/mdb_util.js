var MongoClient = require('mongodb').MongoClient;
var defaultUri  = 'mongodb://localhost:27017/sample';
var _db         = null;

module.exports  = {
    connectToDb: function(callback){
        MongoClient.connect(defaultUri, function(err, db){
            _db = db;
            callback(err);
        });
    },
    getDb: function(){
        return _db;
    }
};