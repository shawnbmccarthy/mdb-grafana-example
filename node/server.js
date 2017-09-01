var express     = require('express');
var bodyParser  = require('body-parser');
var morgan      = require('morgan');
var app         = express();
var mongoUtil   = require('./utils/mdb_util');
var g_route     = require('./routes/grafano');

app.use(morgan('combined'));
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
app.use('/api/v1', g_route);

mongoUtil.connectToDb(function(err){
    if(err){
        console.log('error occurred');
        console.log(err);
        return;
    }
    app.listen(3333, function(){
        console.log('grafano 2 mongodb api running on port 3333');
    });
});