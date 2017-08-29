var express = require('express');
var router = express.Router();

router.all('/', function(req, res) {
  console.log(req.body);
  res.json({results: 'success'});
  res.end();
});

router.all('/search', function(req, res){
  console.log(req.body);
  var result = [];
  res.json(result);
  res.end();
});

router.all('/annotations', function(req, res) {
  console.log(req.body);
  res.json([]);
  res.end();
});

router.all('/query', function(req, res){
  console.log(req.body);
  var tsResult = [];
  res.json(tsResult);
  res.end();
});

module.exports = router;