var express     = require('express');
var grafanaUtil = require('../utils/grafana_utils');
var router      = express.Router();

router.get('/', function(req, res) {
  res.json({results: 'success'});
  res.end();
});

/*
 * search is called when building the metrics - currently we will focus on
 * timeseries for the minute data - avg value across the various reps
 */
router.post('/search', function(req, res){
    grafanaUtil.generateAcctTypes('minutes', function(err, result){
        if(err){
            res.status(500);
            res.json({error: 'failed to generate reps for query'});
            res.end();
        } else {
            res.json(result);
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
    grafanaUtil.generateAcctTypeDataPoints('minutes', req.body, function(err, results){
        if(err){
            console.log(err);
            res.status(500);
            res.json({error: 'failed to generate reps for query'});
            res.end();
        } else {
            res.json(results);
            res.end();
        }
    });
});

module.exports = router;