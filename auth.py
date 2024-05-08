# login code
# Signup code
# Rendering form
# Routing
# Javascript
import mysql.connector
from DBAPI import dbAPI

class user_auth:

    
    def signup(user, password, email):
        connection = dbAPI.get_db_connection()
        cursor = dbAPI.get_db_cursor(connection)
        signup_query = "INSERT INTO accounts (username,password,email) VALUES (%s, %s, %s)"
        response = cursor.execute(signup_query, (user,password, email,))
        connection.commit()
        connection.close()
        return response

    