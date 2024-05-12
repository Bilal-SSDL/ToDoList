# login code
# Signup code
# Rendering form
# Routing
# Javascript
import mysql.connector
from DBAPI import dbAPI
from flask import jsonify



dbapi = dbAPI("tasktodo")
class user_auth:

    #def __init__(self):   

    #dbapi = dbAPI("tasktodo")

    @staticmethod
    def signup(user, password, email):
        connection = dbapi.get_db_connection()
        cursor = dbapi.get_db_cursor(connection)
        # will add user already exists logic here
        signup_query = "INSERT INTO accounts (username,password,email) VALUES (%s, %s, %s)"
        cursor.execute(signup_query, (user,password, email,))
        connection.commit()
        connection.close()
        return "success"
        #return jsonify({"message": "Task Updated successfully"}), 200

    @staticmethod
    def signin(user, password):
        connection = dbapi.get_db_connection()
        cursor = dbapi.get_db_cursor(connection)
        # will add user already exists logic here
        signin_query = "SELECT * from accounts where (username) VALUES (%s)"
        cursor.execute(signin_query, (user,))
        data = cursor.fetchall()
        #if user == data.index[]
        connection.close()
        return "success"

    