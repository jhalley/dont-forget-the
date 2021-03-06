angular.module('groceryApp', ['ngTouch'])
  .controller('GroceryController', ['$scope', '$http', function($scope, $http) {
    // FOR DEBUGGING
    window.scope = $scope;
    
    // MAIN VARIABLES 
    var d = new Date();
    $scope.new_list_name = 'Grocery List ' + d.getFullYear() + '-' + ('0' + (d.getMonth()+1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2);
    $scope.new_list_item_name = '';
    $scope.list_selected = '';
    $scope.list = [];
    $scope.list_items = [];
    $scope.view_mode = 'lists'; // lists, List_items
    $scope.recurring_get_list_items = false;
    
    // Functions
    $scope.view_lists = function(){
      $scope.view_mode = 'lists';
      clearInterval($scope.recurring_get_list_items);
      $scope.recurring_get_list_items = false;
    }
    
    $scope.view_list_items = function(l){
      $scope.get_list_items(l);
      $scope.view_mode = 'list_items';
    }
    
    $scope.toggle_list_item_status = function(li){
      li.bought = !li.bought;
      $http.get('/grocery/api/list_item/' + li.id + '/toggle/').
       success(function(data, status, headers, config) {
         // this callback will be called asynchronously
         // when the response is available
         //$scope.get_list_items($scope.list_selected);
         console.log('Success');
       }).
       error(function(data, status, headers, config) {
         // called asynchronously if an error occurs
         // or server returns response with an error status.
         alert('Error accessing site. Please refresh page.')
       });
    }
    
    $scope.get_list_items = function(l){
      $scope.list_selected = l;
      $http.get('/grocery/api/list/' + l.id).
       success(function(data, status, headers, config) {
          // this callback will be called asynchronously
          // when the response is available
          $scope.list_items = data['data'];
          
          if (!$scope.recurring_get_list_items && $scope.view_mode == 'list_items'){
            $scope.recurring_get_list_items = setInterval(function(){ // Polling
                $scope.get_list_items($scope.list_selected);
            }, 3000);
          };
       }).
       error(function(data, status, headers, config) {
         // called asynchronously if an error occurs
         // or server returns response with an error status.
         alert('Error accessing site. Please refresh page.')
       });
    };
    
    $scope.add_new_list_item = function(){
      $http.post('/grocery/api/list_item/', {
          name: $scope.new_list_item_name,
          l_id: $scope.list_selected.id,
        }, {
          headers: {'X-CSRFToken': $.cookie('csrftoken')},
        }).
        success(function(data, status, headers, config) {
          // this callback will be called asynchronously
          // when the response is available
          $scope.get_list_items($scope.list_selected);  // todo: need to make this more efficient
          $scope.new_list_item_name = '';
          $('#addNewListItemModal').modal('toggle');
        }).
        error(function(data, status, headers, config) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
          alert('Error creating new list item.')
        });
    }
    
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
      
    // INIT
    $scope.get_list();
      
      
  }]);