from flask import Flask, jsonify, request, Response
from phonebook_ent import phonebook_entities
import json

app = Flask(__name__)
print(__name__)

def valid_phonebook_entity(phonebook_entity):
    if (
        "name" in phonebook_entity and
        "last_name" in phonebook_entity and
        "phonenumber" in phonebook_entity and
        "birthday" in phonebook_entity and
        "country" in phonebook_entity and
        'city' in phonebook_entity):
        return True
    else:
        return False

#GET /phonebook
@app.route('/phonebook')
def get_all_phonebook_entities():
    return jsonify({'phonebook' : phonebook_entities})

#GET /phonebook/<phone_number>
@app.route('/phonebook/<int:phone_number>')
def get_phonebook_entity(phone_number):
    return_value = {}
    for phonebook_entity in phonebook_entities:
        if phonebook_entity['phonenumber'] == phone_number:
            return_value = {
                'name': phonebook_entity['name'],
                'last_name': phonebook_entity['last_name'],
                'phonenumber': phonebook_entity['phonenumber'],
                'email': phonebook_entity['email'],
                'birthday': phonebook_entity['birthday'],
                'country': phonebook_entity['country'],
                'city': phonebook_entity['city']
            }
    return jsonify(return_value)

#POST /phonebook
@app.route('/phonebook', methods = ['POST'])
def add_phonebook_entity():
    request_data = request.get_json()
    if(valid_phonebook_entity(request_data)):
        new_phonebook_entity = {
            'name': request_data['name'],
            'last_name': request_data['last_name'],
            'phonenumber': request_data['phonenumber'],
            'email': request_data['email'],
            'birthday': request_data['birthday'],
            'country': request_data['country'],
            'city': request_data['city']
        }
        phonebook_entities.insert(0, new_phonebook_entity)
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/phonebook/" + str(new_phonebook_entity['phonenumber'])
        return response
    else:
        invalid_phonebook_object_error_message = {
            "error" : "Invalid phonebook object passed in request",
        }
        response = Response(json.dumps(invalid_phonebook_object_error_message), 400, mimetype='application/json')
        return (response)

#PUT /phonebook/<phonenumber>
@app.route('/phonebook/<int:phone_number>', methods = ['PUT'])
def replace_phonebook_entity(phone_number):
    request_data = request.get_json()
    new_phonebook_entity = {
        'name': request_data['name'],
        'last_name': request_data['last_name'],
        'phonenumber': phone_number,
        'email': request_data['email'],
        'birthday': request_data['birthday'],
        'country': request_data['country'],
        'city': request_data['city']
    }
    i = 0
    for phonebook_entity in phonebook_entities:
        current_phonenumber = phonebook_entity["phonenumber"]
        if current_phonenumber == phone_number:
            phonebook_entities[i] = new_phonebook_entity
        i += 1
    response = Response("", 204)
    return response

#PATCH /phonebook/<phonenumber>
@app.route('/phonebook/<int:phone_number>', methods = ["PATCH"])
def update_phonebook_entity(phone_number):
    request_data = request.get_json()
    updated_phonebook_entity = {}
    if("name" in request_data):
        updated_phonebook_entity["name"] = request_data["name"]
    if ("last_name" in request_data):
        updated_phonebook_entity["last_name"] = request_data["last_name"]
    if ("email" in request_data):
        updated_phonebook_entity["email"] = request_data["email"]
    if ("birthday" in request_data):
        updated_phonebook_entity["birthday"] = request_data["birthday"]
    if ("country" in request_data):
        updated_phonebook_entity["country"] = request_data["country"]
    if ("city" in request_data):
        updated_phonebook_entity["city"] = request_data["city"]

    for phonebook_entity in phonebook_entities:
        if phonebook_entity["phonenumber"] == phone_number:
            phonebook_entity.update(updated_phonebook_entity)
    response = Response("", 204)
    response.headers['Location'] = str(phone_number)
    return response

#DELETE /phonebook/<phonenumber>
@app.route('/phonebook/<int:phone_number>', methods = ["DELETE"])
def delete_phonebook_entity(phone_number):
    i = 0
    deleted_count = 0
    for phonebook_entity in phonebook_entities:
        if phonebook_entity["phonenumber"] == phone_number:
            phonebook_entities.pop(i)
            response = Response("", status = 204)
            deleted_count += 1
        i += 1
    invalid_phonebook_object_error_message = {
        "error": "Phonebook entity that was provided was not found, so therefore unable to delete"
    }
    if deleted_count == 0:
        response = Response(json.dumps(invalid_phonebook_object_error_message), status = 404, mimetype = 'application/json')
    return response;

if __name__ == "__main__":
    app.run(port=5000)

