from sql_connection import get_sql_connection
def fetch_address(connection, user_id):
    cursor = connection.cursor()
    query = "SELECT address FROM gs.user_profiles where user_id = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    address = result[0]
    return address

def updateAddress(connection, data):
    address_str = ", ".join([str(value) for value in data.values()])
    cursor = connection.cursor()
    query = "update gs.user_profiles set address = %s where user_id = %s"
    input = (data['address'], data['city'], data['state'], data['pincode'])
    cursor.execute(address_str, data['user_id'])
    connection.commit()

if __name__=="__main__":
    connection = get_sql_connection()
    print(updateAddress(connection, {"address": "asdsa",
        "city": "delhi",
        "state": "dsdc",
        "pincode": "1223",
        "user_id": 1 }))
