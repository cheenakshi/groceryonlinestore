from flask import Flask, request, jsonify
import json
from user_profile import add_profile, fetch_email
import product_doa, uom_dao, order_dao
from signup import signup_acc
from login import login_acc
from cartItems_dao import addToCarts, showItems, deleteItem
from order_dao import fetch_address
from sql_connection import get_sql_connection
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required , get_jwt_identity
from datetime import timedelta

app = Flask(__name__)
# Configure JWT
app.config['JWT_SECRET_KEY'] = 'cheenu'  # Replace with a secure key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialize JWTManager with the Flask app
jwt = JWTManager(app)
CORS(app)
connection = get_sql_connection()

@app.route('/getProducts')
def getAllproducts():
    products = product_doa.get_all_products(connection)
    response = jsonify(products)
    return response

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    print('Inserting product')
    request_payload = request.get_json()
    print(f"Request payload: {request_payload}")
    product_id = product_doa.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    request_payload = request.get_json()
    product_id = request_payload.get('product_id')
    return_id = product_doa.delete_product(connection, product_id)
    response = jsonify({
        'product_id': return_id
    })
    return response


@app.route('/signup', methods = ['POST'])
def signup():
    request_payload = request.get_json()
    signup_resp = signup_acc(connection, request_payload)
    response=jsonify({
        'message': signup_resp
    })
    return response

@app.route('/login', methods = ['POST'])
def login():
    request_payload = request.get_json()
    email = request_payload.get('email')
    password = request_payload.get('password')
    access_token, name, signup_id, user_id, login_response = login_acc(connection, email, password)
    if access_token:
        response = jsonify({
            'message': login_response,
            'access_token': access_token,
            'name':name,
            'signup_id':signup_id,
            'user_id':user_id
        })
    else:
        response = jsonify({
            'message': login_response
        })
    return response

@app.route('/addToCart', methods=['POST'])
@jwt_required()
def addToCart():
    current_user = get_jwt_identity()
    print(current_user)
    request_payload = request.get_json()
    request_payload['user_id'] = current_user.get('user_id')
    cart_response = addToCarts(connection, request_payload)
    response = jsonify({
        'message': "Product added to cart",
        'cartItemId': cart_response
    })
    return response

@app.route('/viewCart', methods=['GET'])
@jwt_required()
def view_cart():
    current_user = get_jwt_identity()
    user_id = current_user.get('user_id')
    cart_response = showItems(connection, user_id)
    response=jsonify(cart_response)
    return response

@app.route('/deleteItem', methods=['POST'])
def delete_item():
    request_payload = request.get_json()
    cart_id = request_payload.get('cartItemId')
    item_response = deleteItem(connection, cart_id)
    response = jsonify({
        'message':item_response
    })
    return response

@app.route('/userProfile', methods=['POST'])
def users_profiles():
    request_payload = request.get_json()
    response =add_profile(connection, request_payload)
    return response

@app.route('/getEmail' , methods = ['POST'])
def get_email():
    request_payload = request.get_json()
    email = fetch_email(connection, request_payload)
    response = jsonify({
        'email' : email
    })
    return response

@app.route('/getAddress', methods = ['GET'])
@jwt_required()
def get_address():
    current_user = get_jwt_identity()
    user_id = current_user.get('user_id')
    address = fetch_address(connection, user_id)
    response = jsonify({
        "address":address
    })
    return response

@app.route('/updateAddress', methods=['POST'])
@jwt_required()
def update_address():
    current_user = get_jwt_identity()
    user_id = current_user.get('user_id')
    request_payload = request.get_json()
    request_payload["user_id"] = user_id


if __name__ == "__main__":
    print("Starting grocery management system ")
    app.run(port= 5000)