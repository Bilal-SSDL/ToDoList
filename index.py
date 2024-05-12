from flask import Flask, render_template, request, jsonify, redirect, url_for
from DBAPI import dbAPI
from app import app_blueprint
from auth import user_auth

app_inst = Flask(__name__)
app_inst.register_blueprint(app_blueprint)
db_api = dbAPI('tasktodo')
#usr_auth = user_auth()


@app_inst.route("/" , methods=['GET', 'POST'])
def home():

   #  if request.method == "GET":   
        user = request.args.get("username")
        password = request.args.get("password")
        
        if user:
           connection = db_api.get_db_connection()
           db_api.create_auth_table()
           connection.close() 
           response = user_auth.signin(user, password)
           if response == "success":
                return render_template('home.html')
           else:
                return response
        else:
           return render_template('login.html')

@app_inst.route("/signup" , methods=['GET', 'POST'])
def signup():
        if request.method == "POST":
                user = request.json.get("username")
                password = request.json.get("password")
                email = request.json.get("email")
                response = user_auth.signup(user, password, email)
                if response == "success":
                       return render_template('login.html')
                else:
                       return render_template('signup.html')
        else:
           return render_template('signup.html')
if __name__ == "__main__":
    app_inst.run(debug=True)