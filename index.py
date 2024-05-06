from flask import Flask, render_template, request, jsonify
from DBAPI import dbAPI

app_inst = Flask(__name__)

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

if __name__ == "__main__":
    app_inst.run(debug=True)