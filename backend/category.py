from sql_connection import get_sql_connection
def fetch_category(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM categories"
    cursor.execute(query)
    results = cursor.fetchall()
    categories =[]
    for row in results:
        category = {
            "category_id":row[0],
            "category_name":row[1],
            "category_image":row[2]
        }
        categories.append(category)
    return categories

if __name__ == "__main__":
    connection = get_sql_connection()
    print(fetch_category(connection))