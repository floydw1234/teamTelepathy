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

    $scope.person = '';


/*
0 = starting
1 = capturing data
2 = results
3 = game
*/
    $scope.status  = {stat: 0};
    console.log("asdf");


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


	$scope.result = function(){
		$http.get("/result")
		.success(function(data){
			console.log("Welcome " + data.person);
			$scope.person = data.person;
		})
		.error(function(data,status,headers,config){
			$scope.ResponseDetails = JSON.stringify({data: data});
	    });
	}

    $scope.result();


}]);
