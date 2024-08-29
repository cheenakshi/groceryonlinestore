from sql_connection import get_sql_connection
import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def signup_acc(connection, data):
    cursor = connection.cursor()
    hashed_password = hash_password(data['password'])
    signup_query = ("insert into signup (name, email, password) values (%s,%s,%s)")
    signup_data = (data['name'], data['email'], hashed_password)
    cursor.execute(signup_query,signup_data)
    
    connection.commit()
    return "register successfully"

