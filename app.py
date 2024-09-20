# Working with API's

from flask import Flask, jsonify, request
from data_dict_simple import simple

app = Flask(__name__)



# routes, CRUD operations, GET, POST, PUT, PATCH. DELETE

@app.route('/members', methods=['GET'])  # GET (automaticly GET if no method is specified)
def read_all():
    return jsonify(simple)



# exercises: get members by id
@app.route('/members/<int:id>', methods=['GET'])  # GET method (operator) 
def read_member(id):
    # 'simple' is a list of dictionaries, and each dictionary has an 'id' key
    member = next((item for item in simple if item.get("id") == id), None)
    if member:
        return jsonify(member)
    else:
        return jsonify({"error": "Member not found"}), 404



# exercises: change students to member
@app.route('/members', methods=['POST'])  # POST method (operator) 
def create_member():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    
    # Append the new member to the simple list
    simple.append(data)
    
    return jsonify(simple), 201



# remove a member from the list using the id
@app.route('/members/<int:id>', methods=['DELETE'])  # DELETE method (operator) 
def delete_member(id):
    # 'simple' is a list of dictionaries, and each dictionary has an 'id' key
    member = next((item for item in simple if item.get("id") == id), None)
    if member:
        simple.remove(member)
        return jsonify({"message": f"Member with id: {id}, is successfully deleted"}), 200
    else:
        return jsonify({"error": "Member not found"}), 404



# use PUT to change the value in an object
@app.route('/members/<int:id>', methods=['PUT'])  # PUT method (operator)
def update_member(id):
    # Find the member with the  ID
    member = next((item for item in simple if item.get("id") == id), None)

    if not member:
        return jsonify({"error": "Member not found"}), 404

    # Get the new data from the request
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    # Update the member's data completely (PUT replaces the whole resource)
    member['id'] = data.get('id', member['id'])  # Replace if if provided, else keep the current one
    member['first_name'] = data.get('first_name', member['first_name'])  # Same for name

    return jsonify({"message": f"Member with id: {id} is successfully updated", "member": member}), 200


# use PATCH to change the value in an object
@app.route('/members/<int:id>', methods=['PATCH'])  # PATCH method (operator)
def change_member(id):
    # Find the member with the given ID
    member = next((item for item in simple if item.get("id") == id), None)

    if not member:
        return jsonify({"error": "Member not found"}), 404

    # Get the new data from the request
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    # Update the member's data completely (PUT replaces the whole resource)
    member['id'] = data.get('id', member['id'])  # Replace if if provided, else keep the current one
    member['first_name'] = data.get('first_name', member['first_name'])  # Same for name

    return jsonify({"message": f"Member with id: {id} is successfully updated", "member": member}), 200

if __name__ == '__main__':
    app.run(debug=True)
