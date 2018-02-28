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
		if($scope.currentUser != ''){
			console.log("asdf");
			var data = {
				"user": $scope.currentUser
			};
			$http.post("/dataCapture",data)
			.success(function(data){
				console.log("doing the thing");
			})
			.error(function(data,status,headers,config){
				$scope.ResponseDetails = JSON.stringify({data: data});
		    });
		}else{
			alert("You gotta go back and choose who you are! Com'on breh");
		}

	}
	var url = "url(clown.jpg)"
	$scope.switchPicture = function(url){
		var doc = document.getElementById("image");
		setTimeout(function(){
			doc.style.backgroundImage = url;
		},10000);

	}
	$scope.switchPicture(url);
	setTimeout(function(){
			$scope.switchPicture("url(black.jpeg)");
	},10000);

	/*\
	httpget = function(callback){
	do the request. then{
	when it is ready{
		callback(data);
}
	}

}

	*/

	$scope.getUsers = function(){
	    $http.get('/userList')
		.success(function(data){
			$scope.userList = data.users;
			console.log(data.users)
	    })
		.error(function(data,status,headers,config){
			$scope.ResponseDetails = JSON.stringify({data: data});
	    });
	};
	$scope.selectUser = function(user){
		$scope.currentUser = user;
	}
}]);
