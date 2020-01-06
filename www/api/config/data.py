import json
import xlrd
import os
from bottle import abort

def make_data(c,type_data):
    rH = [x[0] for x in c.description]
    rs = c.fetchall()   
    data_json=[]
    for r in rs:
        data_json.append(dict(zip(rH,r)))
    if type_data == 'object':
        data = data_json[0]
    elif type_data == 'array':
        data = data_json
    return data

def make_data_excel(file):
    if file:
        filename = file.filename
        ext = filename.split('.')[1]
        if os.path.exists(filename):
            os.remove(filename)
        else:
            file.save(filename)
        try:
            wb = xlrd.open_workbook(filename)
            sh = wb.sheet_by_index(0)
            rH=['product_name','product_desc','category_id']
            data=[]
            start_row = 1
           
            for x in range(0,sh.nrows):
                #row x col pertama kosong
                if sh.cell_value(x,0) == "":
                    pass
                #row x col pertama termasuk field rH
                elif sh.cell_value(x,0) in rH:
                    #data mula setelah field r+1
                    start_row = x+1
                    break
                #deteksi row 
                else:
                    start_row = x
                    break
            # row data dimulai dari 1
            for r in range(start_row,sh.nrows):
                data.append(dict(zip(rH,sh.row_values(r))))
            if data:                  
                os.remove(filename)
        except:
            os.remove(filename)
            abort(400)
    return data  

    
def response_api(data):
    return (
        json.dumps(data)
    )