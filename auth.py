# login code
# Signup code
# Rendering form
# Routing
# Javascript
import mysql.connector
from DBAPI import dbAPI
from flask import jsonify, session



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
        #signin_query = "SELECT * from accounts where username = %s"
        signin_query = "SELECT * from accounts where username = %s AND password = %s"
        cursor.execute(signin_query, (user,password,))
        data = cursor.fetchone()
        connection.close()
        if data:
            #session["loggedin"] = True
            #session["id"] = data['id']
            #session["username"] = data['username']
            return "success"
        else:
            return "Incorrect username/password!"
        #if user == data.index[]
         
        #return "success"

    