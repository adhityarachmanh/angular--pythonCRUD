
import json
from bottle import Bottle
from config.data import response_api

app = Bottle()
from views.products import products
app.merge(products)
from views.categories import categories
app.merge(categories)

@app.route("/creator")
def index():
    return 'Adhitya Rachman H'


@app.error(400)
def bad_request(e):
    return response_api({
        'code': 400,
        'message': 'Ada kekeliruan input saat melakukan request.',
        'data': None
    })

@app.error(404)
def not_found(e):
    return response_api({
        'code': 404,
        'message': 'Data tidak berhasil ditemukan.',
        'data': None
    })

@app.error(405)
def method_not_allowed(e):
    return response_api({
        'code': 405,
        'message': 'Data tidak berhasil ditemukan.',
        'data': None
    })


@app.error(500)
def internal_server_error(e):
    return response_api({
        'code': 500,
        'message': 'Mohon maaf, ada gangguan pada server kami.',
        'data': None
    })
