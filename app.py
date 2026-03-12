from flask import Flask, jsonify, request
from flask_cors import CORS

import config
import crud

app = Flask(__name__)

# Load configuration
app.config['SECRET_KEY'] = config.SECRET_KEY
CORS(app)

# Register routes
@app.route('/')
def index():
    return "Hello from Flask!"

@app.route("/todos", methods=["POST"])
def create_todo_route():
    # create
    return {}

@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo_route(todo_id):
    # get
    task = crud.get_todo_by_id(todo_id) # task or None
    if task is None:
        return jsonify({"error":"Task not found"}), 404

    return jsonify(task), 200

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo_route(todo_id):
    # update
    task = crud.get_todo_by_id(todo_id) # task or None
    if task is None:
        return jsonify({"error":"Task not found"}), 404

    update_data = request.get_json()
    updated_task = crud.update_todo(todo_id, update_data)
    
    return jsonify(updated_task), 200

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo_route(todo_id):
    # delete
    task = crud.get_todo_by_id(todo_id) # task or None
    if task is None:
        return jsonify({"error":"Task not found"}), 404
    crud.delete_todo(todo_id)
    
    return jsonify({"message":"Delete process success"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
