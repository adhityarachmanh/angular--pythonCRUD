app.directive('appNavbar',function () {
    return{
        restrict:'E',
        templateUrl:'views/includes/navbar.html',
        controller:'navbar-controller'
    }
}).controller('navbar-controller',['$scope',function ($scope) {
    $scope.name='Navbar'
}])