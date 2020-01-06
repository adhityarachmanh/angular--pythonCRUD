
from datetime import datetime
from bottle import abort,request
from config.conn import create_connection_db
from config.data import make_data,make_data_excel

def get(id=None,is_set=False):
    with create_connection_db("aws") as conn:
        c = conn.cursor()
        if id:
            query = f"SELECT * FROM products WHERE product_id={id}"
            try:
                c.execute(query)
                res = make_data(c,'object')
            except:
                abort(404)
        else:
            query = "SELECT * FROM products"
            try:
                c.execute(query)
                res = make_data(c,'array')
            except:
                abort(404)
        c.close()
    conn.close()
    if res:
        res={
            'code':200,
            'message':'Data Products Telah Ditemukan.',
            'products':res
        }
        if is_set:
            res['code']=202
            res['message']='Data Products Telah Tersimpan'
    return res
       

def post():
    created_at = datetime.now()
    with create_connection_db("aws") as conn:
        c = conn.cursor()
        query = """
            INSERT INTO 
            products 
            (product_name,product_desc,category_id,created_at)
            VALUES 
            (%s,%s,%s,%s)
            """
        if request.files:
            # INPUT EXCEL FILE
            excel = request.files['file']
            data_excel = make_data_excel(excel)
            for req in data_excel:
                try:
                    c.execute(query,(req['product_name'],req['product_desc'],req['category_id'],created_at))
                    conn.commit()
                except:
                    conn.close()
                    abort(404)
            res = {
                'code':200,
                'message':'Data Excel Berhasil Di Input.',
                'data_excel':data_excel
            }
        elif request.json:
             # INPUT REQ JSON DATA
            req = request.json
            try:
                c.execute(query,(req['product_name'],req['product_desc'],req['category_id'],created_at))
                conn.commit()
                try:
                    find_lastrow = "SELECT product_id FROM products ORDER BY product_id DESC LIMIT 1"
                    c.execute(find_lastrow)
                    lastrow_id = make_data(c,'object')['product_id']
                    res = get(lastrow_id,True)
                except:
                    conn.close()
                    abort(404)
            except:
                conn.close()
                abort(404)
    conn.close()
    return res

def put(id):
    return 'PUT'

def delete(id=None):
    with create_connection_db("aws") as conn:
        c = conn.cursor()
        if id:
            query = f"DELETE FROM products WHERE product_id={id}"
            try:
                data_delete = get(id)
                c.execute(query)
                conn.commit()
                res = data_delete
            except:
                conn.close()
                abort(400)
        else:
            query = "DELETE FROM products"
            try:
                c.execute(query)
                conn.commit()
                restart_seq = "ALTER SEQUENCE products_product_id_seq RESTART WITH 1"
                try:
                    c.execute(restart_seq)
                    res = {
                        'code':200,
                        'message':"semua data products berhasil dihapus."
                    }
                except:
                    conn.close()
                    abort(400)
            except:
                conn.close()
                abort(400)
    conn.close()
    return res

