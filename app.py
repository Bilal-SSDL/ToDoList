from flask import Flask, render_template, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
import sqlite3

app_inst = Flask(__name__)

# initiaize the database
# app_inst.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://todo.db'
# db = SQLAlchemy(app_inst)
def get_db_connection():
    connection = sqlite3.connect('tasktodo.db')
    connection.row_factory = sqlite3.Row
    return connection

def get_db_cursor(connection):
    cursor = connection.cursor()
    return cursor

def create_db_table():
    connection = get_db_connection()
    cursor = get_db_cursor(connection)
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                   id INTEGER PRIMARY_KEY,
                   task TEXT
    )''')
    connection.commit()
    connection.close()

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     db.create_all()


@app_inst.route("/" , methods=['GET', 'POST'])
def home():
    #return "To-Do List Home Page"
    return render_template('home.html')

@app_inst.route("/add", methods=['GET', 'POST'])
def add_task():
    if request.method == "POST":
        task = request.json.get("task")
        create_db_table()
        connection = get_db_connection()
        cursor = get_db_cursor(connection)
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        connection.commit()
        connection.close()
        return jsonify({"message": "Task added successfully"}), 200
    elif request.method == "GET":
        return render_template("add_task.html")

@app_inst.route("/update", methods=['GET', 'POST'])
def update_task():
    return render_template('update_task.html')

@app_inst.route("/delete", methods=['GET', 'POST'])
def delete_task():
    return render_template('delete_task.html')

if __name__ == "__main__":
    app_inst.run(debug=True)