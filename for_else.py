people = [{'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 22},
        {'name': 'Peter', 'age': 30},
        {'name': 'Jenifer', 'age': 28}]
name  = input('Enter a name: ')
for person in people:
    if person['name'].lower() == name.lower():
        print(person['name'])
        break
else:
    print("Person not found")