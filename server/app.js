var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var bodyParser = require('body-parser');
var request = require("request-promise");
var PythonShell = require('python-shell');
var fs = require('fs');



var result = "";




var app = express();
app.use(bodyParser.urlencoded({ extended: false}));
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));




// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');




// error handler
app.get("/", function(req,res){
	res.sendfile('public/recognise.html');
});


app.get("/training", function(req,res){
	res.sendfile('public/training.html');
});

app.get("/result", function(req,res){
	res.sendfile('public/result.html');
});

app.get("/game", function(req,res){
	res.sendfile('public/game.html');
});


app.get("/averages", function(req,res){
	var array = [];
	var model = mongoose.model('average2', avgS, 'averages');
		model.find().exec(function(err,avgs){
			avgs.forEach(function(thing){
				array.push(thing);
			});
			res.send(array);
		});
});

app.get("/userList", function(req,res){
    var content = fs.readFileSync("users.json");
    res.send(JSON.parse(content));
});
app.get("/allValues", function(req,res){
	var array = [];
	var model = mongoose.model('id', values, 'ids');
		model.find().exec(function(err,values){
			values.forEach(function(thing){
				array.push(thing);
			});
			res.send(array);
		});
});


app.post("/recognisePerson",function(req,res){

	PythonShell.run('py/Identification.py', function (err) {
  		if (err) throw err;
		res.send("success!");
	});



});

app.get("/getResult",function(req,res){
	setTimeout(function(){
	fs.readFile("output.txt", {encoding: 'utf-8'}, function(err,data){

    if (!err){
        console.log('received data: ' + data);
		res.send({person: data});
    }else {
        console.log(err);
    }
});


	},3000);
});


app.post("/dataCapture",function(req,res){

    var options = {
      args: [req.body.user]
    };
    PythonShell.run('py/test.py',options, function (err) {
  		if (err) throw err;
		res.send("success!");
	});



});


var datesToUnix = function(date){
	var dates = date.split("-");
	dates[0] = dates[0].replace(/^\s\s*/, '').replace(/\s\s*$/, '');
	dates[1] = dates[1].replace(/^\s\s*/, '').replace(/\s\s*$/, '');
	return [Math.floor(Date.parse(dates[0])/1000), Math.floor(Date.parse(dates[1])/1000)];
};




module.exports = app;
app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
});
