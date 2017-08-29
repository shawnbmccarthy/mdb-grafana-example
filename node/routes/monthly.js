var express     = require('express');
var grafanaUtil = require('../utils/grafana_utils');
var router      = express.Router();

router.get('/', function(req, res) {
    res.json({results: 'success'});
    res.end();
});

router.post('/search', function(req, res){
    grafanaUtil.generateReps('monthly', function(err, result){
        if(err){
            res.json({error: 'failed to generate reps for query'});
            res.sendStatus(500);
        }
        res.json(result);
        res.end();
    });
});

router.post('/annotations', function(req, res) {
    console.log(req.body);
    res.json([]);
    res.end();
});

router.post('/query', function(req, res){
    grafanaUtil.generateRepsDataPoints('hourly', req.body, function(err, results){
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