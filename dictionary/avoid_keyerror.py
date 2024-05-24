fruits = {'apple': 1, 'orange': 3}
fruits.setdefault('bananas', 0)
fruits['bananas'] += 1
print(fruits)
