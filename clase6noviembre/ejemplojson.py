import json

# Convertir un objeto Python a una cadena JSON
data = {
    'key1': 'value1',
    'key2': 'value2'
}

json_string = json.dumps(data)
print(json_string)

# Convertir una cadena JSON a un objeto Python
data = json.loads(json_string)
print(data)