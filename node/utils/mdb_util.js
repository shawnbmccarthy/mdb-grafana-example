var MongoClient = require('mongodb').MongoClient;

var env = process.env.NODE_ENV || 'development';
var cfg = require('../config/' + env);
var _db         = null;

module.exports  = {
    connectToDb: function(callback){
        MongoClient.connect(cfg.url, function(err, db){
            _db = db;
            callback(err);
        });
    },
    getDb: function(){
        return _db;
    }
};