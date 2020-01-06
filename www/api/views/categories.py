from bottle import Bottle,request
from config.data import response_api
from methods.categories import get

categories = Bottle()

@categories.route("/categories",method=['GET'])

def categories_api():
    if request.method == 'GET':
        data = get()
    return response_api(data)