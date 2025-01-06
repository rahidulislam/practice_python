fruits={'apple':10,'banana':5,'orange':30}
key = None
while True:
    try:
        key = input("Enter a key to lookup")
        fruit = fruits[key.lower()]
    except KeyError:
        print(f"Key {key} not found")
    else:
        print(f"Value for key {key} is {fruit}")
        break
    finally:
        print("Done")