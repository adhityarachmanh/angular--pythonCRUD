from bottle import abort
from config.conn import create_connection_db
from config.data import make_data

def get():
    with create_connection_db("aws") as conn:
        c = conn.cursor()
        query = "SELECT * FROM categories"
        try:
            c.execute(query)
            res = make_data(c,'array')
        except:
            abort(404)
    conn.close()
    if res:
        res = {
            'code':200,
            'message':'Categories Telah Di Temukan',
            'categories':res
        }    
    return res
