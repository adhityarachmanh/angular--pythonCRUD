app.service('categories-service',['$http',function (http) {
    const api = "/api/categories"
    this.get =function () {
        return http({
            method:'GET',
            url:api
        })
    }
}])