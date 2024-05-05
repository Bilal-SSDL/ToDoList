from flask import Flask, render_template, request, jsonify
from DBAPI import dbAPI
#from flask_sqlalchemy import SQLAlchemy


app_inst = Flask(__name__)
#dbAPI class instance
db_api = dbAPI('tasktodo')

class home:
        
    @app_inst.route("/" , methods=['GET', 'POST'])
    def home():
        connection = db_api.get_db_connection()
        cursor = db_api.get_db_cursor(connection)
        db_api.create_db_table()
        cursor.execute("SELECT * FROM tasks_new")
        data = cursor.fetchall()     
        connection.close()
        print(data)
        #for row in data:
        return render_template('home.html', tasks=data)

    @app_inst.route("/add", methods=['GET', 'POST'])
    def add_task():
        if request.method == "POST":
            task = request.json.get("task")
            db_api.create_db_table()
            connection = db_api.get_db_connection()
            cursor = db_api.get_db_cursor(connection)
            insert_query = "INSERT INTO tasks_new (task) VALUES (%s)"
            cursor.execute(insert_query, (task,))
            connection.commit()
            connection.close()
            return jsonify({"message": "Task added successfully"}), 200
        elif request.method == "GET":
            return render_template("add_task.html")

    @app_inst.route("/update", methods=['GET', 'PUT'])
    def update_task():
        if request.method == "PUT":
            task = request.json.get("task")
            id = request.json.get("id")
            print("Task ", task)
            print("ID ", id)
            connection = db_api.get_db_connection()
            cursor = db_api.get_db_cursor(connection)
            update_query = "UPDATE tasks_new SET task= %s where id = %s"
            cursor.execute(update_query, (task, id,))
            connection.commit()
            connection.close()
            return jsonify({"message": "Task Updated successfully"}), 200
        elif request.method == "GET":
            return render_template('update_task.html')

    @app_inst.route("/delete", methods=['GET', 'DELETE'])
    def delete_task():
        if request.method == "DELETE":
            id   = request.json.get("id")
            connection = db_api.get_db_connection()
            cursor = db_api.get_db_cursor(connection)
            delete_query = "DELETE FROM tasks_new WHERE id= %s"
            cursor.execute(delete_query, ( id,))
            connection.commit()
            connection.close()
            return jsonify({"message": "Task Deleted successfully"}), 200
        elif request.method == "GET":
            return render_template('delete_task.html')

    if __name__ == "__main__":
        app_inst.run(debug=True)