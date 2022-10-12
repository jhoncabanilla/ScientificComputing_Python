import json

data = '''{
    "name" : "Jhon",
    "phone" : {
        "type" : "intl",
        "number" : "+1 722 233 2349"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

# json.loads() parsea el String y nos devuelve un diccionario
info = json.loads(data)
print(info["name"])
print(info["phone"]["number"])
print(info["email"]["hide"])