# from flask import Flask, render_template, request, jsonify
# from database import dbAPI

# app_inst = Flask(__name__)

# #dbAPI class instance
# db_api = dbAPI('tasktodo.db')


# @app_inst.route("/" , methods=['GET', 'POST'])
# def home():

#         connection = db_api.get_db_connection()
#         cursor = db_api.get_db_cursor(connection)
#         data = cursor.execute("SELECT * FROM tasks_new").fetchall()
#         connection.close()
#         print(data)
#         return render_template('home.html', tasks=data)

# if __name__ == "__main__":
#     app_inst.run(debug=True)