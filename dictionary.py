# empty_dict = {}
# print(type(empty_dict))

# create a dictionary
# person = {
#     'name':'John',
#     'age':30,
#     'city':'New York'
# }
# print(person['name'])
# print(person['active'])
# ssn = person.get('ssn', 'N/A')
# print(ssn)
# person['gender'] = 'Male'
# print(person)

# update a dictionary
# person['age']=35
# print(person)
# del person['gender']
# print(person)

# loop through a dictionary
# print(person.items())
# for key,value in person.items():
#     print(f"{key}={value}")

# loop through keys
# for key in person.keys():
#     print(key)
# for key in person:
#     print(key)
# loop through values
# for value in person.values():
#     print(value)

# dictionary comprehension
stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}
# using normal for loop

new_stocks ={}
for symbol,price in stocks.items():
    new_stocks[symbol] = price *1.02
print(new_stocks)

# using dictionary comprehension
new_stocks = {symbol:price*1.02 for (symbol,price) in stocks.items()}
print(new_stocks)

# using for loop to filter items
selected_stocks = {}
for symbol,price in stocks.items():
    if price >100:
        selected_stocks[symbol] = price
print(selected_stocks)

# using dictionary comprehension to filter items
selected_stocks = {symbol:price for (symbol,price) in stocks.items() if price>100}
print(selected_stocks)