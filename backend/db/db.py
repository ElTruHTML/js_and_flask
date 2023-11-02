
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
    connection.close()
    return f"{todo} wurde eingetragen"

def fetch_all_todos():
    connection = sqlite3.connect("todo-db.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    sql = "SELECT name, done FROM todos"
    cursor.execute(sql)

    fetchedTodos = cursor.fetchall()
    connection.close()
    print(type(fetchedTodos))

    allEntries = []
    for row in fetchedTodos:
        allEntries.append({"name": row["name"], "done": row["done"]})

    return allEntries