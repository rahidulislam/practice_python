bonuses = [25, 100, 200, 300, 45]
# for bonus in map(lambda x: x * 2, bonuses):
#     print(bonus)
double = map(lambda bonus: bonus * 2 if bonus % 2 == 0 else bonus, bonuses)
print(list(double))

# convert names to uppercase
names = ["John", "Paul", "George", "Ringo"]
new_names = map(lambda name: name.capitalize(), names)
print(list(new_names))

# calculate tax
carts = [["smartphone", 400], ["tablet", 300], ["laptop", 500]]
TAx = 0.1
new_carts = map(lambda item: [item[0], item[1], item[1] * TAx], carts)
print(list(new_carts))

# convert strings to integers
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
new_numbers = map(int, numbers)
print(list(new_numbers))

# square numbers
numbers = [1, 2, 3, 4, 5]
new_numbers = map(lambda number: number**2, numbers)
print(list(new_numbers))

# length of words
words = ["apple", "banana", "cherry", "date", "elderberry"]
new_words = map(len, words)
# new_words = map(lambda word:len(word), words)
print(list(new_words))

# convert celsius to fahrenheit
celsiuses = [0, 20, 37, 100]
fahrenheit = map(lambda celsius: (celsius * 9 / 5) + 32, celsiuses)
print(list(fahrenheit))

# combine two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_list = map(lambda x, y: x + y, list1, list2)
print(list(new_list))

# Filter out None values
data = [1, None, 3, None, 5, None]
new_data = map(lambda x: x if x is not None else "N/A", data)
print(list(new_data))

# calculate areas of circles
radius = [1, 2, 3, 4]
area = map(lambda r: 3.14 * r**2, radius)
print(list(area))

# reverse string
words = ["hello", "world", "python"]
new_words = map(lambda word: word[::-1], words)
print(list(new_words))

# multiply each element by a constant
nums = [1, 2, 3, 4]
CONSTANT = 10
new_nums = map(lambda num: num * CONSTANT, nums)
print(list(new_nums))

# extract domain names from email
emails = ["8lH3H@google.com", "2v4dM@facebook.com", "Tt4f9@twitter.com"]
domains = map(lambda email: email.split("@")[1], emails)
print(list(domains))

# normalize data
users = [
    {"id": 1, "name": "ALICE"},
    {"id": 2, "name": "BOB"},
    {"id": 3, "name": "CHARLIE"},
]
normalize_users = map(
    lambda user: {"id": user["id"], "name": user["name"].capitalize()}, users
)
print(list(normalize_users))

# flatten nested tuples
nested_tuples = [(1, 2), (3, 4), (5, 6)]
flattened_tuples = map(lambda t: list(t), nested_tuples)
print(list(flattened_tuples))

# calculate grades
students = [
    {"name": "Alice", "scores": [85, 90, 92]},
    {"name": "Bob", "scores": [78, 81, 85]},
    {"name": "Charlie", "scores": [88, 89, 93]},
]
students_grade = map(
    lambda student: {
        "name": student["name"],
        "scores": student["scores"],
        "average": sum(student["scores"]) / len(student["scores"]),
    },
    students,
)
print(list(students_grade))

# map function dynamically
nums = [2, 4, 6, 8]
functions = [lambda x: x**2, lambda x: x**3, lambda x: x / 2, lambda x: x + 10]
new_nums = map(lambda x, function: function(x), nums, functions)
print(list(new_nums))

# transform JSON data
data = {"a": "10", "b": "20", "c": "30"}
json_data = map(lambda k: (k[0], int(k[1])), data.items())
print(dict(json_data))

# process date strings
dates = ["18-12-2022", "19-12-2022", "20-12-2022"]
new_dates = map(
    lambda date: {
        "day": date.split("-")[0],
        "month": date.split("-")[1],
        "year": date.split("-")[2],
    },
    dates,
)
print(list(new_dates))

# filter and transform 
users = [
    {"name":"Alice", "active":True},
    {"name":"Bob", "active":False},
    {"name":"Charlie", "active":True},
]
active_users = map(lambda user: user["name"], filter(lambda user: user["active"], users))
print(list(active_users))

