
import os, sys, sqlite3

def create_new_todo(todo):
    connection = sqlite3.connect("todo-db.db")
    cursor = connection.cursor()

    sql = "CREATE TABLE IF NOT EXISTS todos (" \
        "id INT PRIMARY_KEY AUTO_INCREMENT, " \
        "name VARCHAR(20) NOT NULL," \
        "done INT NOT NULL)"
    print(sql)
    cursor.execute(sql)
    return f"{todo} von der neuen Fn"