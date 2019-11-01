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

valid_entity = {"name" : "Guta",
		"last_name" : "Shuhart",
        "phonenumber" : 12311111112,
        "email" : "guta.shuhart@harmont.rp",
        "birthday" : "19.05.1932",
        "country" : "Canada",
        "city" : "Harmont"
    }

missing_name = {"last_name" : "Shuhart",
        "phonenumber" : 12311111112,
        "email" : "guta.shuhart@harmont.rp",
        "birthday" : "19.05.1932",
        "country" : "Canada",
        "city" : "Harmont"
    }
missing_last_name = {"name" : "Guta",
        "phonenumber" : 12311111112,
        "email" : "guta.shuhart@harmont.rp",
        "birthday" : "19.05.1932",
        "country" : "Canada",
        "city" : "Harmont"
    }
missing_phonenumber = {"name" : "Guta",
		"last_name" : "Shuhart",
        "email" : "guta.shuhart@harmont.rp",
        "birthday" : "19.05.1932",
        "country" : "Canada",
        "city" : "Harmont"
    }
missing_email = {"name" : "Guta",
		"last_name" : "Shuhart",
        "phonenumber" : 12311111112,
        "birthday" : "19.05.1932",
        "country" : "Canada",
        "city" : "Harmont"
    }
missing_birthday = {"name" : "Guta",
		"last_name" : "Shuhart",
        "phonenumber" : 12311111112,
        "email" : "guta.shuhart@harmont.rp",
        "country" : "Canada",
        "city" : "Harmont"
    }
missing_country = {"name" : "Guta",
		"last_name" : "Shuhart",
        "phonenumber" : 12311111112,
        "email" : "guta.shuhart@harmont.rp",
        "birthday" : "19.05.1932",
        "city" : "Harmont"
    }
missing_city = {"name" : "Guta",
		"last_name" : "Shuhart",
        "phonenumber" : 12311111112,
        "email" : "guta.shuhart@harmont.rp",
        "birthday" : "19.05.1932",
        "country" : "Canada",
    }

assert valid_phonebook_entity(valid_entity) == True, "Should be True"
assert valid_phonebook_entity(missing_name) == False, "Should be False"
assert valid_phonebook_entity(missing_last_name) == False, "Should be False"
assert valid_phonebook_entity(missing_email) == True, "Should be True"
assert valid_phonebook_entity(missing_birthday) == False, "Should be False"
assert valid_phonebook_entity(missing_country) == False, "Should be False"
assert valid_phonebook_entity(missing_city) == True, "Should be True"

