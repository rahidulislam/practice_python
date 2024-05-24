alien_0 = {
    "color": "green",
    "points": 5
}
print(f"The alien is {alien_0['color']}")
alien_0["color"] = "yellow"
print(f"The alien is now {alien_0['color']}")
alien = {}
alien['color'] = 'green'
alien['points'] = 5
print(alien)
alien_1 = {'color':'green', 'points':5}
for key,value in alien_1.items():
    print(f"Key is : {key} value is : {value}")
del alien_1['points']
print(alien_1)
