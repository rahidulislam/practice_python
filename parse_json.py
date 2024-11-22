import json

# convert/parse json to python object
# player1 ='{"name":"Carlos","age":35,"city":"porto"}'
# x = json.loads(player1)
# print(x["name"])
# print(x["age"])

# convert python object to json
player2 = {
    "name": "Rahidul",
    "age": 35,
    "city": "porto"
}
# y = json.dumps(player2)
# print(y)
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(66))
# print(json.dumps(12.34))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# parse json from a file
with open("practice_python/player.json") as f:
    json_data = json.load(f)

print(json_data)

# write a json to a file
with open("practice_python/player1.json", "w") as f:
    json.dump(player2, f, indent=4, sort_keys=True)