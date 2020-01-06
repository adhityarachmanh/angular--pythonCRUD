app.service('products-service', ['$http', function (http) {
    let api = '/api/products'
    this.get = function (id) {
        let url = api;
        if (id) url += '/' + id
        return http({
            method: 'GET',
            url: url
        })
    }
    this.post = function (data, type) {
        let url = api;
        if (type == 'FORM') return http.post(url, data)
        else if (type == 'EXCEL') return http.post(url, data, {
            headers: {
                'Content-Type': undefined
            }, transformRequest: angular.indentity
        })
    }
    this.delete =function(id){
        let url = api;
        if (id) return http.delete(url+'/'+id)
        else return http.delete(url)
    }
  

    
}])