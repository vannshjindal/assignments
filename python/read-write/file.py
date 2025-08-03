# import json
# with open("data.json", "r") as data:
#    file = json.load(data)
# print(file)

import json
with open("data.json", "r") as file:
    data = json.load(file)  
new_user = {
    "id": 4,
    "name": "Charlie",
    "email": "charlie@example.com"
}
data.append(new_user)
with open("data.json", "w") as file:
    json.dump(data, file)


