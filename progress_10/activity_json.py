import json

person = {
    'name': 'Amaru Jamiu'
    'Age': 42,
    'status': 'married',
    'children': ['yaro', 'Ahmed'],
    'salary': 120000
}

person_json = json.dumps(person)
print(person)