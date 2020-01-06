from bottle import Bottle,request
from methods.products import get,post,put,delete
from config.data import response_api

products = Bottle()

@products.route("/products",method=['GET','POST','DELETE'])
@products.route("/products/<id:int>",method=['GET','PUT','DELETE'])
def products_api(id=None):
    if request.method == 'GET':
        data = get(id)
    elif request.method == 'POST':
        data = post()
    elif request.method == 'PUT':
        data = put(id)
    elif request.method == 'DELETE':
        data = delete(id)
    return response_api(data)
