angular.module('groceryApp', [])
  .controller('GroceryController', ['$scope', '$http', function($scope, $http) {
    // FOR DEBUGGING
    window.scope = $scope;
    
    // MAIN VARIABLES 
    $scope.list = []
    
    // INIT
    $http.get('/grocery/api/list').
      success(function(data, status, headers, config) {
        // this callback will be called asynchronously
        // when the response is available
        $scope.list = data['data'];
      }).
      error(function(data, status, headers, config) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
      });
      
    //$scope.todos = [
    //  {text:'learn angular', done:true},
    //  {text:'build an angular app', done:false}];
      
  }]);