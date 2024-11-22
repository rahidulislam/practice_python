# colors = ['red', 'green', 'blue', 'yellow', 'black']
# red, green,blue = colors
# print(red, green,blue)
# red,green, *other = colors
# print(red,green,other)

cites = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen']
# for city in cites:
#     print(city)

# for city in enumerate(cites):
#     print(city)

# for index, city in enumerate(cites):
#     print(f"{index}: {city}")

# result = cites.index('bd')
# print(result)
# city = 'Beijing'
# if city in cites:
#     result = cites.index(city)
#     print(result)
# else:
#     print(f"{city} is not in the list")

# colors = ['red', 'green', 'blue', 'yellow', 'black']
# colors_iter = iter(colors)
# color = next(colors_iter)
# print(colors_iter)
# print(color)
# color = next(colors_iter)
# print(color)
# color = next(colors_iter)
# print(color)
# color = next(colors_iter)
# print(color)
# color = next(colors_iter)
# print(color)
# color = next(colors_iter)
# print(color)
# print(next(colors_iter))
# for color in colors_iter:
#     print(color)

bonuses =[1000, 2000, 3000, 4000]
# new_bonuses = []
# for bonus in bonuses:
#     new_bonuses.append(bonus * 2)

# print(new_bonuses)
def double(bonus):
    return bonus * 2
iterator = map(double, bonuses)
print(list(iterator))
