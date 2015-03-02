angular.module('groceryApp', ['ngTouch'])
  .controller('GroceryController', ['$scope', '$http', function($scope, $http) {
    // FOR DEBUGGING
    window.scope = $scope;
    
    // MAIN VARIABLES 
    var d = new Date();
    $scope.new_list_name = 'Grocery List ' + d.getFullYear() + '-' + ('0' + (d.getMonth()+1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2);
    $scope.list = []
    
    // INIT
    $scope.get_list = function(){
      $http.get('/grocery/api/list').
       success(function(data, status, headers, config) {
         // this callback will be called asynchronously
         // when the response is available
         $scope.list = data['data'];
       }).
       error(function(data, status, headers, config) {
         // called asynchronously if an error occurs
         // or server returns response with an error status.
         alert('Error accessing site. Please refresh page.')
       });
    };
    $scope.get_list();
      
    // Functions
    $scope.add_new_list = function(){
      $http.post('/grocery/api/list/', {
          name: $scope.new_list_name,
        }, {
          headers: {'X-CSRFToken': $.cookie('csrftoken')},
        }).
        success(function(data, status, headers, config) {
          // this callback will be called asynchronously
          // when the response is available
          $scope.get_list();
          $('#addNewListModal').modal('toggle');
        }).
        error(function(data, status, headers, config) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
          alert('Error creating new list.')
        });
    }
      
    //$scope.todos = [
    //  {text:'learn angular', done:true},
    //  {text:'build an angular app', done:false}];
      
  }]);