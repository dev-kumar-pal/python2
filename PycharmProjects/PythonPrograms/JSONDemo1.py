import json

#Reading a JSON file
'''person_dict = {'name': 'Bob','age': 12,'children': None}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)'''

#Writing json to a file
person_dict = {"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}

with open('Person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)