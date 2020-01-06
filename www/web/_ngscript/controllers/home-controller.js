app.controller("home-controller", ['$scope', '$timeout', 'products-service', 'categories-service', function ($scope, setTimeout, ps, cs) {
    $scope.name = "home-controller"
    $scope.dataHeader = {
        product_name: 'product_name',
        product_desc: 'product_desc',
        category_id: 'category_id',
        created_at: 'created_at'
    }
    /**
     * Select Category
     */
    $scope.select_category = function (e) {
        let c_id = parseInt(e.value)
        if (c_id !== 0 && $scope.category_selected !== c_id) {
            const products = $scope.products.filter(data => data.category_id = c_id)
            $scope.category_selected = c_id
            $scope.prodcuts = products
            setTimeout(() => {
                loaded_products()
            }, 1000)
        }
    }
    /**
    * POP UP Gambar
    */
    $scope.imagePopUp = function (product_id) {
        ps.get(product_id).then(function successCallback({ data: { products } }) {
            angular.element("#product-image").modal("show")
            $scope.modal_data = products
        })
    }
    /**
    * find category
    */
    $scope.find_category = function (category_id) {
        return $scope.categories.find(item => item.category_id = category_id)['category_name']
    }
    /**
    * EXCEL
    */
    $scope.upload_excel = function (element) {

        fd = new FormData()
        fd.append('file', element.files[0])


        ps.post(fd, 'EXCEL').then(function successCallback(response) {
            console.log(response)
            loaded_products()
        }).catch(function failedCallback(response) {
            console.log(response)
        })
    }

    /**
     * DELETE ALL
     */
    $scope.delete = function (id) {
        if (id) ps.delete(id).then(function successCallback(response) {
            console.log(response)
            loaded_products()
        })
        else ps.delete().then(function successCallback(response) {
            console.log(response)
            loaded_products()
        })

    }
    function loaded_products() {
        $scope.loading = true
        setTimeout(function () {
            ps.get().then(function successCallback({ data: { products } }) {
                $scope['products'] = products
                $scope.loading = false
            })
        }, 1500)
    }

    function loaded_categories() {
        cs.get().then(function successCallback({ data: { categories } }) {
            $scope['categories'] = categories
        })
    }
    loaded_categories()
    loaded_products()
}])