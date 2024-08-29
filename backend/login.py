from sql_connection import get_sql_connection
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from datetime import timedelta
import bcrypt

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'cheenu'  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

jwt = JWTManager(app)

def check_password(hashed_password, password):
    # Convert the password to bytes before checking
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# def login_acc(connection, email, password):
#     with app.app_context():  # Ensure app context is available
#         cursor = connection.cursor()
#         query = 'SELECT password, name, signup_id FROM gs.signup WHERE email = %s'
#         cursor.execute(query, (email,))
#         result = cursor.fetchone()

#         if result:
#             hashed_password, name, signup_id = result
#             if check_password(hashed_password, password):
#                 # Create an access token
#                 access_token = create_access_token(identity={"email": email, "name": name})
#                 return access_token, name, signup_id, "Login successful"
#             else:
#                 return None, "Login unsuccessful: incorrect password"
#         else:
#             return None, "Login unsuccessful: email not found"

def login_acc(connection, email, password):
    with app.app_context():  # Ensure app context is available
        cursor = connection.cursor()
        # Fetch password, name, signup_id, and user_id in one query
        query = '''
            SELECT s.password, s.name, s.signup_id, u.user_id 
            FROM gs.signup s 
            LEFT JOIN gs.user_profiles u ON s.signup_id = u.signup_id 
            WHERE s.email = %s
        '''
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        if result:
            hashed_password, name, signup_id, user_id = result
            if check_password(hashed_password, password):
                # Include both signup_id and user_id in the access token
                access_token = create_access_token(identity={
                    "email": email, 
                    "name": name, 
                    "signup_id": signup_id, 
                    "user_id": user_id
                })
                return access_token, name, signup_id, user_id, "Login successful"
            else:
                return None, None, None, None, "Login unsuccessful: incorrect password"
        else:
            return None, None, None, None, "Login unsuccessful: email not found"


if __name__ == "__main__":
    connection = get_sql_connection()
    with app.app_context():  # Ensure app context is available
        print(login_acc(connection, 'r@gmail.com', 'Radha@12345'))
