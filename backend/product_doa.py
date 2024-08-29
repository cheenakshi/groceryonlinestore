import mysql.connector
from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("Select products.product_id, products.name, products.uom_id, products.price_per_unit, products.category, products.image_url, uom.uom_name from products inner join uom on uom.uom_id = products.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, category, image_url, uom_name) in cursor:
        response.append({
            'product_id':product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'category':category,
            'uom_name' : uom_name,
            'image_url' : image_url
        })
    return(response)

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit, category, image_url)"
             "VALUES (%s, %s, %s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'], product['category'], product['image_url'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("Delete from products where product_id = "+ str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))
    