var express      = require('express');
var bodyParser   = require('body-parser');
var morgan       = require('morgan');
var app          = express();
var mongoUtil    = require('./utils/mdb_util');
var grafanaRoute = require('./routes/grafana');

var env = process.env.NODE_ENV || 'development';
var cfg = require('./config/' + env);

app.use(morgan(cfg.format));
app.use(bodyParser.json());

/*
 * setup headers for grafano datasource
 */
app.use(function(req, res, next){
  res.setHeader('Access-Control-Allow-Headers', 'accept, content-type');
  res.setHeader('Access-Control-Allow-Methods', 'POST');
  res.setHeader('Access-Control-Allow-Origin', '*');
  next();
});

/*
 * setup routes
 */
app.use('/api/v1', grafanaRoute);

mongoUtil.connectToDb(function(err){
    if(err){
        console.log('error occurred');
        console.log(err);
        return;
    }
    app.listen(cfg.port, function(){
        console.log('grafano 2 mongodb api running on port 3333');
    });
});