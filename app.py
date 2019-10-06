from flask import Flask, jsonify

app = Flask(__name__)
print(__name__)

phonebook_entities = [
    {
        'name' : 'Redrik',
        'last_name' : 'Shuhart',
        'phonenumber' : 12311111111,
        'email' : 'redrik.shuhart@harmont.rp',
        'birthday' : '19.01.1931',
        'country' : 'Canada',
        'city' : 'Harmont'
    },
    {
        'name': 'Richard',
        'last_name': 'Nunan',
        'phonenumber': 12311231611,
        'email': 'richard.nunan@harmont.rp',
        'birthday': '15.04.1918',
        'country': 'Canada',
        'city': 'Harmont'
    }
]

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

app.run(port=5000)

