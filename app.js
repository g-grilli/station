var express = require('express');
var app = express();
var session = require('express-session');
var pgp = require('pg-promise')({
 promiseLib: Promise
});
var db = pgp({
 database: 'zipcode',
 user: 'postgres'
});
var Chart = require('chart.js');

 
var apicache = require('apicache');
var cache = apicache.middleware;
 
var axios = require('axios');

app.set('view engine', 'hbs');
app.use('/static', express.static('public'));
app.use('/axios', express.static('node_modules/axios/dist'));
app.use('/chart.js', express.static('node_modules/chart.js/dist'));
app.use(session({
  secret: process.env.SECRET_KEY || 'dev',
  resave: true,
  saveUninitialized: false,
  cookie:{maxAge: null}
}));
 
app.get('/', function (request, response) {
 response.render('main.hbs', {zip_code: request.session.zip_code || '77379'});
});

app.get('/forecast', function (request, response) {
response.render('forecast.hbs', {zip_code: request.session.zip_code || '77379'});
});

app.get('/sevenday', function (request, response) {
response.render('sevenday.hbs', {zip_code: request.session.zip_code || '77379'});
});

app.get('/city', function (request, response) {
 response.render('city.hbs', {query: request.query});
});

app.get('/raspberry', function (request, response) {
 response.render('raspberry.hbs', {});
}); 
 
app.get('/api', cache('60 minutes'), function (request, response, next) {
 var zip_code = request.query.zip_code;
 request.session.zip_code = zip_code;
 console.log('Generating new response', zip_code);
 var dbdata;
 db.any(`
  SELECT lat, long, location_text FROM data
  WHERE zipcode = $1 AND location_type = 'PRIMARY'`, zip_code)
    .then(function(resultsArray) {
     console.log('results', resultsArray);
     dbdata = resultsArray[0];
     return axios.get(`https://api.darksky.net/forecast/8a1d95b8dc652cbcfad9cff1b79e5194/${dbdata.lat},${dbdata.long}`);
     })
     .then(function (darksky) {
     response.json({db: dbdata, ds: darksky.data});
     })
     .catch(next);
 });
 
app.get('/outlook', cache('60 minutes'), function (request, response, next) {
 var outlook = request.query.outlook;
 console.log('Generating new response', outlook);
 var dbdata;
 db.any(`
  SELECT lat, long, location_text FROM data
  WHERE zipcode = $1 AND location_type = 'PRIMARY'`, outlook)
    .then(function(resultsArray) {
     console.log('results', resultsArray);
     dbdata = resultsArray[0];
     return axios.get(`https://api.darksky.net/forecast/8a1d95b8dc652cbcfad9cff1b79e5194/${dbdata.lat},${dbdata.long}`);
     })
     .then(function (darksky) {
     response.json({db: dbdata, ds: darksky.data});
     })
     .catch(next);
 });
 
app.get('/local', function (request, response, next) {
 var records = request.query.records;
 console.log(records);
 db.any(`
  SELECT temp_h, temp_p, humidity, pressure, datetime FROM sensor_data
  ORDER BY datetime DESC LIMIT 1`, records)
  .then(function(results) {
    response.render('local.hbs', {results: results});
     
  })
     .catch(next);
 });
 
app.get('/custom', function (request, response, next) {
 var custom = request.query.custom;
 console.log(custom);
 db.any(`
  SELECT temp_h, temp_p, humidity, pressure, datetime FROM sensor_data
  ORDER BY datetime DESC LIMIT $1`, custom)
  .then(function(results) {
    var data = [];
    var dataTP = [];
    var dataH = [];
    var dataP = [];
    var dataD =[];
    results.forEach(function (r) {
      data.push(r.temp_h);
      dataTP.push(r.temp_p);
      dataH.push(r.humidity);
      dataP.push(r.pressure);
      
    });
    response.render('custom.hbs', {results: results, data: JSON.stringify(data),dataTP: JSON.stringify(dataTP),dataH: JSON.stringify(dataH), dataP: JSON.stringify(dataP), dataD: JSON.stringify(dataD)})
     
  })
     .catch(next);
 }); 
 
 
 
 
var PORT = process.env.PORT || 80;
 app.listen(PORT, function () {
   console.log('I am awakening... I feel awake... I am alive on PORT ' + PORT + '!');
});

