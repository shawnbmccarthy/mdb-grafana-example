var express     = require('express');
var grafanaUtil = require('../utils/grafana_utils');
var router      = express.Router();

router.get('/:dim/:t/', function(req, res) {
    res.json({results: 'success'});
    res.end();
});

router.post('/:dim/:t/search', function(req, res){
    grafanaUtil.generateDims(req.params.t, req.params.dim, function(err, result){
        if(err){
            res.json({error: 'failed to generate reps for query'});
            res.sendStatus(500);
        }
        res.json(result);
        res.end();
    });
});

router.post('/:dim/:t/annotations', function(req, res) {
  res.json([]);
  res.end();
});

router.post('/:dim/:t/query', function(req, res){
    grafanaUtil.generateDataPoints(req.params.t, req.params.dim, req.body, function(err, results){
        if(err){
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