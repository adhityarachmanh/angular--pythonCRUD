app.controller('add-product-controller', ['$scope', 'products-service','categories-service','$location', function ($scope, ps,cs,location) {
    $scope.name = "Add Product"
    $scope.product = {}
    $scope.product_submit = function (product) {
        ps.post(product,'FORM')
        .then(function successCallback(response) {
            console.log(response)
            location.path("/")
        }).catch(function failedCallback({message}) {
            console.log(message)
        })
    }
    function loaded_categories() {
        cs.get().then(function successCallback({data:{categories}}) {
            $scope['categories'] = categories
        
        }).catch(function failedCallback({message}) {
            console.log(message)
        })
    }
    loaded_categories()
}])

// $scope.image_upload = function (files) {

    //     var fileReader = new FileReader();
    //     fileReader.onload = function (e) {
    //         var srcData = e.target.result
    //         var img = document.createElement("img")
    //         var imgContainer = document.querySelector("#img-response")

    //         $scope.product.product_img=srcData;

    //         img.src = srcData
    //         img.style = 'width:100%;height:300px;'

    //         imgContainer.innerHTML = img.outerHTML
    //     };
    //     fileReader.readAsDataURL(files[0]);
    // }