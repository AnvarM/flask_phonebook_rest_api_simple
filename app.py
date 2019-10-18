from flask import Flask, jsonify, request, Response
import json
from settings import *
from PhonebookModel import *
from test import valid_phonebook_entity
import jwt
import datetime
from UserModel import User
from functools import wraps


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        try:
            jwt.decode(token, app.config['SECRET_KEY'])
            return f(*args, **kwargs)
        except:
            return jsonify({'error': 'Provide a valid token to view this page'}), 401
    return wrapper


@app.route('/login', methods = ['POST'])
def get_token():
    request_data = request.get_json()
    username = str(request_data['username'])
    password = str(request_data['password'])
    match = User.username_password_match(username, password)

    if match:
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
        token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256')
        return token

    else:
        return Response("", 401, mimetype = 'application/json')


#GET /phonebook
@app.route('/phonebook')
def get_all_phonebook_entities():
    return jsonify({'phonebook' : Phonebook.get_all_records()})

#GET /phonebook/<phone_number>
@app.route('/phonebook/<int:phone_number>')
def get_phonebook_entity(phone_number):
    return_value = Phonebook.get_record(phone_number)
    return jsonify(return_value)

#POST /phonebook
@app.route('/phonebook', methods = ['POST'])
@token_required
def add_phonebook_entity():
    request_data = request.get_json()
    if(valid_phonebook_entity(request_data)):
        Phonebook.add_record(request_data['name'],
                             request_data['last_name'],
                             request_data['phonenumber'],
                             request_data['email'],
                             request_data['birthday'],
                             request_data['country'],
                             request_data['city'])
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/phonebook/" + str(request_data['phonenumber'])
        return response
    else:
        invalid_phonebook_object_error_message = {
            "error" : "Invalid phonebook object passed in request",
        }
        response = Response(json.dumps(invalid_phonebook_object_error_message), 400, mimetype='application/json')
        return (response)

#PUT /phonebook/<phonenumber>
@app.route('/phonebook/<int:phone_number>', methods = ['PUT'])
@token_required
def replace_phonebook_entity(phone_number):
    request_data = request.get_json()
    Phonebook.replace_record(phone_number,
                             request_data['name'],
                             request_data['last_name'],
                             request_data['email'],
                             request_data['birthday'],
                             request_data['country'],
                             request_data['city'])
    response = Response("", 204)
    return response



#PATCH /phonebook/<phonenumber>
@app.route('/phonebook/<int:phone_number>', methods = ["PATCH"])
@token_required
def update_phonebook_entity(phone_number):
    request_data = request.get_json()
    updated_phonebook_entity = {}
    if("name" in request_data):
        Phonebook.update_record_name(phone_number, request_data['name'])
    if ("last_name" in request_data):
        Phonebook.update_record_last_name(phone_number, request_data['last_name'])
    if ("email" in request_data):
        Phonebook.update_record_email(phone_number, request_data['email'])
    if ("birthday" in request_data):
        Phonebook.update_record_birthday(phone_number, request_data['birthday'])
    if ("country" in request_data):
        Phonebook.update_record_country(phone_number, request_data['country'])
    if ("city" in request_data):
        Phonebook.update_record_city(phone_number, request_data['city'])

    response = Response("", 204)
    response.headers['Location'] = str(phone_number)
    return response

#DELETE /phonebook/<phonenumber>
@app.route('/phonebook/<int:phone_number>', methods = ["DELETE"])
@token_required
def delete_phonebook_entity(phone_number):
    if Phonebook.delete_record(phone_number):
        response = Response("", status = 204)
        return response
    invalid_phonebook_object_error_message = {
        "error": "Phonebook entity that was provided was not found, so therefore unable to delete"
    }
    response = Response(json.dumps(invalid_phonebook_object_error_message), status = 404, mimetype = 'application/json')
    return response;

if __name__ == "__main__":
    app.run(port=5000)

