import mysql.connector

def sql_connection():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="contoh_pakan"
    )
    cursor = db_connection.cursor()
    return db_connection, cursor