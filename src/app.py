"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


rabadan_family = FamilyStructure("Rabadan") # Create the jackson family object

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException) 
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/') 
def sitemap():
    return generate_sitemap(app)


# Get all family members
@app.route('/members', methods=['GET']) 
def handle_members():
    response_body = {}
    members = rabadan_family.get_all_members()
    response_body ["family"] = members
    return response_body, 200


# Get one member
@app.route('/members/<int:id>', methods=['GET']) 
def get_member(id):
    response_body = {}
    result = rabadan_family.get_member(id)
    response_body ["message"] = "Usuario encontrado"
    response_body ["results"] = result
    return response_body, 200


# Add member
@app.route('/members', methods=['POST']) 
def add_members():
    data = request.json
    members = rabadan_family.add_member(data)
    response_body = {"result" : data }
    return response_body, 200


#Delete member
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    result = rabadan_family.delete_member(member_id)

    if result:
        response_body = {"result": "Member deleted successfully"}
        return response_body, 200
    else:
        response_body = {"result": "Member not found"}
        return response_body, 404


# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
