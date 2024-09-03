from sql_connection import get_sql_connection
import bcrypt

def hash_password(password):
    # Generate a salt and hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # Convert the hash to a string format suitable for storing in the database
    return hashed_password.decode('utf-8')

def signup_acc(connection, data):
    cursor = connection.cursor()
    hashed_password = hash_password(data['password'])
    signup_query = ("insert into signup (name, email, password) values (%s,%s,%s)")
    signup_data = (data['name'], data['email'], hashed_password)
    cursor.execute(signup_query,signup_data)
    
    connection.commit()
    return "register successfully"

