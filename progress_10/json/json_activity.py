import json

person = {
    'Name': 'Amaru Jamiu',
    'Age': 42,
    'Status': 'Married',
    'Children': ['Yaro', 'Ahmed'],
    'Salary': 120000
}

with open('person.json', 'a') as file:
    json.dump(person, file)