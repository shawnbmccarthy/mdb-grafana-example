var express     = require('express');
var bodyParser  = require('body-parser');
var morgan      = require('morgan');
var app         = express();
var mongoUtil   = require('./utils/mdb_util');
var minutes_rep = require('./routes/minutes_rep');
var hourly_rep  = require('./routes/hourly_rep');
var daily_rep   = require('./routes/daily_rep');
var monthly_rep = require('./routes/monthly_rep');
var yearly_rep  = require('./routes/yearly_rep');
var minutes_at  = require('./routes/minutes_acct_type');
var hourly_at   = require('./routes/hourly_acct_type');
var daily_at    = require('./routes/daily_acct_type');
var monthly_at  = require('./routes/monthly_acct_type');
var yearly_at   = require('./routes/yearly_acct_type');

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
app.use('/api/v1/rep/minutes', minutes_rep);
app.use('/api/v1/rep/hourly', hourly_rep);
app.use('/api/v1/rep/daily', daily_rep);
app.use('/api/v1/rep/monthly', monthly_rep);
app.use('/api/v1/rep/yearly', yearly_rep);
app.use('/api/v1/accttype/minutes', minutes_at);
app.use('/api/v1/accttype/hourly', hourly_at);
app.use('/api/v1/accttype/daily', daily_at);
app.use('/api/v1/accttype/monthly', monthly_at);
app.use('/api/v1/accttype/yearly', yearly_at);

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