cities = ["London", "Paris", "Berlin", "Rome", "Madrid"]
city = "mumbai"
if city in cities:
    find_index = cities.index(city)
    print(find_index)
else:
    print("not found")