app.config(function ($routeProvider,$locationProvider) {
    $routeProvider.
    when("/",{
        templateUrl:"views/pages/home.html",
        controller:"home-controller"
    }).
    when("/add-product",{
        templateUrl:"views/pages/products/add-product.html",
        controller:"add-product-controller"
    }).
    when("/signin",{
        templateUrl:"views/pages/auth/signin.html",
        controller:"signin-controller"
    })
    $locationProvider.html5Mode(true)
})