from sql_connection import get_sql_connection

def addToCarts(connection, data):
    cursor = connection.cursor()
    query = 'insert into cartitems(user_id, product_id, quantity , cost) values (%s,%s,%s, %s)'
    query_data = (data['user_id'],data['product_id'], data['quantity'], data['cost'])
    cursor.execute(query, query_data)
    connection.commit()
    return cursor.lastrowid


# def showItems(connection):
#     cursor = connection.cursor()
#     query = 'SELECT p.product_id, p.name, p.price_per_unit, p.category, p.image_url, c.cartItemId, c.quantity FROM gs.products p join gs.cartitems c on p.product_id = c.product_id'
#     cursor.execute(query)
#     results = cursor.fetchall()
#     items =[]
#     for row in results:
#         item={
#             'product_id':row[0],
#             'name':row[1],
#             'price_per_unit':row[2],
#             'category' :row[3],
#             'image_url':row[4],
#             'cartItemId':row[5],
#             'quantity':row[6]
#         }
#         items.append(item)
#     return items

def showItems(connection, user_id):
    cursor = connection.cursor()
    query = '''
        SELECT p.product_id, p.name, p.price_per_unit, p.category, p.image_url, c.cartItemId, c.quantity
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
            'category': row[3],
            'image_url': row[4],
            'cartItemId': row[5],
            'quantity': row[6]
        }
        items.append(item)
    return items


def deleteItem(connection, cartItemId):
    cursor = connection.cursor()
    query = 'DELETE FROM cartitems WHERE cartItemId = %s'
    cursor.execute(query, (cartItemId,))
    connection.commit()

    return "Item deleted from cart with cartItemId: " + str(cartItemId)


if __name__=="__main__":
    connection = get_sql_connection()
    print(showItems(connection, 16))