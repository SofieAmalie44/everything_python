from flask import Flask, jsonify, request
from data_dict_simple import simple

app = Flask(__name__)

# routes, CRUD operations, GET, POST, PUT, PATCH. DELETE

@app.route('/students')  # GET (automaticly GET if no method is specified)
def read_all():
    return jsonify(simple)

@app.route('/students', methods=['POST'])  # POST methos (operator)
def create():
    data = request.get_json()
    simple.append(data)
    
    return jsonify(simple)

app.run()
