from sql_connection import get_sql_connection
def fetch_address(connection, user_id):
    cursor = connection.cursor()
    query = "SELECT address FROM user_profiles where user_id = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    address = result[0]
    return address

def updateAddress(connection, data):
    address_str = ", ".join(map(str, [value for key, value in data.items() if key!="user_id"]))
    cursor = connection.cursor()
    query = "update user_profiles set address = %s where user_id = %s"
    input = (address_str, data['user_id'])
    cursor.execute(query, input)
    connection.commit()
    return "Address updated successfully"

def fetchItems(connection, user_id):
    cursor = connection.cursor()
    query = '''
        SELECT p.product_id, p.name, p.price_per_unit, c.cartItemId, c.quantity
        FROM products p
        JOIN cartitems c ON p.product_id = c.product_id
        WHERE c.user_id = %s
    '''
    cursor.execute(query, (user_id,))
    results = cursor.fetchall()
    items = []
    for row in results:
        item = {
            'product_id': row[0],
            'name': row[1],
            'price_per_unit': row[2],
            'cartItemId': row[3],
            'quantity': row[4]
        }
        items.append(item)
    return items

if __name__=="__main__":
    connection = get_sql_connection()
    print(updateAddress(connection, {"address": "asdsa",
        "city": "delhi",
        "state": "dsdc",
        "pincode": "1223",
        "user_id": 16 }))
