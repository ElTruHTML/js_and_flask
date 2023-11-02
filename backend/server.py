from flask import Flask, request, jsonify
from flask_cors import CORS
from db import db


#instantiate the server
server = Flask(__name__)
server.config.from_object(__name__)

#enable CORS
CORS(server, resources = {r"/*": {"origins": "*"}})

@server.route("/", methods = ["GET"])
def show_status():
    return "Flask Server is online"


@server.route("/create", methods = ["POST"])
def create_todo():
    todo = request.data.decode("utf-8")
    db.create_new_todo(todo)
    return f"TODO {todo} soll erstellt werden"


@server.route("/overview", methods = ["GET"])
def fetch_all_todos():
    fetchedTodos = db.fetch_all_todos()
    response = jsonify(fetchedTodos)
    return response

if __name__ == "__main__":
    server.run()