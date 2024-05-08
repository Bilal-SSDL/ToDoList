from flask import Flask, render_template, request, jsonify, redirect, url_for
from DBAPI import dbAPI
from app import app_blueprint

app_inst = Flask(__name__)

app_inst.register_blueprint(app_blueprint)
#dbAPI class instance
db_api = dbAPI('tasktodo')


@app_inst.route("/" , methods=['GET', 'POST'])
def home():

        connection = db_api.get_db_connection()
        #cursor = db_api.get_db_cursor(connection)
        db_api.create_auth_table()
        #data = cursor.execute("SELECT * FROM tasks_new").fetchall()
        connection.close()
        #print(data)
        return render_template('login.html')
        #return render_template('login.html', tasks=data)

@app_inst.route("/signup" , methods=['GET', 'POST'])
def signup():

       # connection = db_api.get_db_connection()
        #cursor = db_api.get_db_cursor(connection)
       # db_api.create_auth_table()
        #data = cursor.execute("SELECT * FROM tasks_new").fetchall()
        #connection.close()
        #print(data)
        return render_template('signup.html')
        #return render_template('login.html', tasks=data)
if __name__ == "__main__":
    app_inst.run(debug=True)