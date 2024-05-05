from flask import Flask
import mysql.connector

#DB class
class dbAPI:

    def __init__(self, db_name):
        self.db_name = db_name   
    
    def get_db_connection(self):
        # connection = sqlite3.connect(self.db_name)
        # connection.row_factory = sqlite3.Row
        connection = mysql.connector.connect(
            host="localhost",
            user="bilal",
            password="Liverpo0l@334443",
            database="tasktodo"
        )
        return connection

    def get_db_cursor(self, connection):
         cursor = connection.cursor()
         return cursor

    def create_db_table(self):
        connection = self.get_db_connection()
        cursor = self.get_db_cursor(connection)
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks_new (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   task VARCHAR(255) NOT NULL
        )''')
        connection.commit()
        connection.close()
