import json

data = '''[
    {
        "id" : "001",
        "x": "2",
        "name" : "Pet",
        "phone" : {
            "type" : "intl",
            "number" : "+1 738 234 2234"
        }
    },
    {
        "id" : "007",
        "x": "9",
        "name" : "Loiuse",
        "phone" : {
            "type" : "intl",
            "number" : "+1 129 923 1229"
        }
    }
]'''

# Ahora tenemos una lista de diccionarios
info = json.loads(data)

for item in info:
    print('Name:', item["name"])
    print('Id:', item["id"])
    print('x:', item["x"])
    print('number:', item["phone"]["number"])
