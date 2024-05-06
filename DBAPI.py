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

    def create_auth_table(self):
        connection = self.get_db_connection()
        cursor = self.get_db_cursor(connection)
        cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   username VARCHAR(255) NOT NULL,
                   password VARCHAR(255) NOT NULL,
                   email VARCHAR(255) NOT NULL
        )''')
        # cursor.execute('''CREATE TABLE IF NOT EXISTS `accounts` (
	    #                     `id` int(11) NOT NULL AUTO_INCREMENT,
  	    #                     `username` varchar(50) NOT NULL,
  	    #                     `password` varchar(255) NOT NULL,
  	    #                     `email` varchar(100) NOT NULL,
        #                    PRIMARY KEY (`id`)
        #         ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
        # )''')
        connection.commit()
        connection.close()
