
import sqlite3

def create_new_todo(todo):
    connection = sqlite3.connect("todo-db.db")
    cursor = connection.cursor()

    sql = "CREATE TABLE IF NOT EXISTS todos (" \
        "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
        "name VARCHAR(20) NOT NULL," \
        "done INT NOT NULL)"
    print(sql)
    cursor.execute(sql)


    sql = "INSERT INTO todos (" \
        "name, done)" \
        f"VALUES ('{todo}', 0)"
    cursor.execute(sql)
    connection.commit()
    return f"{todo} wurde eingetragen"