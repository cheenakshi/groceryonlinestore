# import mysql.connector

# __cnx = None
# def get_sql_connection():
#     global __cnx
#     if __cnx is None:
#         __cnx = mysql.connector.connect(user='root', password='root',
#                                 host='127.0.0.1',
#                                 database='gs')
        
#     return __cnx
import psycopg2

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = psycopg2.connect(
            database="gs", 
            user="postgres", 
            host='localhost',
            password="1234",
            port=5432
        )
    return __cnx
