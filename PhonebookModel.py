from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

db = SQLAlchemy(app)

class Phonebook(db.Model):
    __tablename__ = 'phonebook'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phonenumber = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(80))
    birthday = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)

    def json(self):
        return {
            'name' : self.name,
            'last_name' : self.last_name,
            'phonenumber' : self.phonenumber,
            'email' : self.email,
            'birthday' : self.birthday,
            'country' : self.country,
            'city' : self.city
        }

    def add_record(_name, _lastname, _phonenumber, _email, _birthday, _country, _city):
        new_record = Phonebook(name = _name,
                  last_name = _lastname,
                  phonenumber = _phonenumber,
                  email = _email,
                  birthday = _birthday,
                  country = _country,
                  city = _city)
        db.session.add(new_record)
        db.session.commit()

    def get_all_records():
        return [Phonebook.json(phonenumber) for phonenumber in Phonebook.query.all()]

    def get_record(_phonenumber):
        return Phonebook.json(Phonebook.query.filter_by(phonenumber = _phonenumber).first())

    def delete_record(_phonenumber):
        is_successfull = Phonebook.query.filter_by(phonenumber = _phonenumber).delete()
        db.session.commit()
        return bool(is_successfull)

    #Update part
    def update_record_name(_phonenumber, _name):
        phonenumber_to_update = Phonebook.query.filter_by(phonenumber = _phonenumber).first()
        phonenumber_to_update.name = _name
        db.session.commit()

    def update_record_name(_phonenumber, _lastname):
        phonenumber_to_update = Phonebook.query.filter_by(phonenumber = _phonenumber).first()
        phonenumber_to_update.last_name = _lastname
        db.session.commit()

    def update_record_email(_phonenumber, _email):
        phonenumber_to_update = Phonebook.query.filter_by(phonenumber=_phonenumber).first()
        phonenumber_to_update.email = _email
        db.session.commit()

    def update_record_birthday(_phonenumber, _birthday):
        phonenumber_to_update = Phonebook.query.filter_by(phonenumber=_phonenumber).first()
        phonenumber_to_update.birthday = _birthday
        db.session.commit()

    def update_record_country(_phonenumber, _country):
        phonenumber_to_update = Phonebook.query.filter_by(phonenumber=_phonenumber).first()
        phonenumber_to_update.country = _country
        db.session.commit()

    def update_record_city(_phonenumber, _city):
        phonenumber_to_update = Phonebook.query.filter_by(phonenumber=_phonenumber).first()
        phonenumber_to_update.city = _city
        db.session.commit()

    def replace_record(_phonenumber, _name, _lastname, _email, _birthday, _city, _country):
        record_to_replace = Phonebook.query.filter_by(phonenumber = _phonenumber).first()
        record_to_replace.name = _name
        record_to_replace.last_name = _lastname
        record_to_replace.email = _email
        record_to_replace.birthday = _birthday
        record_to_replace.country = _country
        record_to_replace.city = _city
        db.session.commit()

    def __repr__(self):
        phonebook_object = {
            'name' : self.name,
            'last_name' : self.last_name,
            'phonenumber' : self.phonenumber,
            'email' : self.email,
            'birthday' : self.birthday,
            'country' : self.country,
            'city' : self.city
        }
        return json.dumps(phonebook_object)