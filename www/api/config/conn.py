import psycopg2

def create_connection_db(db_name):
    return psycopg2.connect(
           user="postgres",
           host="localhost",
           password="Rum@h10310",
           port=5432,
           database=db_name
        )