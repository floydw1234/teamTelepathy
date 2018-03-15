var app = angular.module('myApp',[]);

app.controller('mainController', ['$scope','$http','$q', function($scope, $http,$q){
	$scope.daterange = '';
	$scope.test = 1;
	$scope.test2 = [];
	$scope.PostDataResponse = {};
	$scope.ResponseDetails = {};
	$scope.userList = [];
	$scope.currentUser = "";
	$scope.charts = [];
	$scope.unique = [];
	$scope.test1 = [];
	$scope.data = [];
	var status = 0;


/*
0 = starting
1 = capturing data
2 = results
3 = game
*/
    $scope.status  = {stat: 0};


	$scope.buildCharts = function(){

		var promises = [];

		$scope.unique.forEach(function(type){
					var deferred = $q.defer();
					$scope.prepareData(type);
					var option =[
					{
			  			title: type+" kWh Demand",
			  			//curveType: 'function',
			  			legend: { position: 'bottom' }
					},type];
					deferred.resolve(option);
					promises.push(deferred.promise);
		});
		return $q.all(promises);
	};


	$scope.startCapture = function(){
        $scope.status.stat = 1;
		document.body.backgroundImage = "";
		$scope.switchPicture(url);
        data = {
            "user": "recognise"
        };
		$http.post("/recognisePerson",data)
		.success(function(data){
			console.log("Welcome " + data.person);
			$scope.person = data.person;
		})
		.error(function(data,status,headers,config){
			$scope.ResponseDetails = JSON.stringify({data: data});
	    });


	}
	var url = "url(img/clown.jpg)"
	$scope.switchPicture = function(url){
		var doc = document.getElementById("image");
		doc.style.backgroundImage = "url(img/black.jpg)";
		setTimeout(function(){
			doc.style.backgroundImage = url;
			setTimeout(function(){
					doc.style.backgroundImage = "";
					$scope.status.stat = 2;
					window.location = "/result";
			},10000);
		},10000);
	}



    setInterval(function(){
        console.log($scope.status.stat);
    },2000);

	/*\
	httpget = function(callback){
	do the request. then{
	when it is ready{
		callback(data);
}
	}

}

	*/

}]);
