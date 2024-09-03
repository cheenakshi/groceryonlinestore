from sql_connection import get_sql_connection

def add_profile(connection, data):
    cursor = connection.cursor()
    query = """
    INSERT INTO user_profiles (signup_id, first_name, last_name, date_of_birth, gender, phone_number, address , email) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    profile_data = (data['signup_id'], data['first_name'], data['last_name'], data['date_of_birth'], data['gender'], data['phone_number'], data['address'] , data['email'])
    cursor.execute(query, profile_data)
    connection.commit()

    last_id =  cursor.lastrowid
    return ({"message": "Profile added successfully", "profile_id": last_id}), 201

def fetch_email(connection, data):
    cursor = connection.cursor()
    query = "SELECT email FROM signup WHERE signup_id = %s"
    profile_data = (data['signup_id'],)
    cursor.execute(query, profile_data)
    result = cursor.fetchone()

    if result:
        return result[0]
    else:'Email not found'



if __name__ == "__main__":
    connection = get_sql_connection()
    
    print(fetch_email(connection, {
    "signup_id":1
}))
