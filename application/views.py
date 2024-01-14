from application import app
from flask import request
from flask import jsonify

import uuid

@app.route('/hello')
def home():
    return "Hello, World!"

@app.route('/messages', methods=['POST'])
def example():
    print("new message received")
    task = init_task(request.get_json())
    return jsonify(task), 201

def init_task(data):
    task = {};
    task["message"] = data["message"]
    task["id"] = str(uuid.uuid4())
    return task

