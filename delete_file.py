import os

# if os.path.exists('test.txt'):
#     os.remove('test.txt')
# else:
#     print("The file does not exist")

try:
    os.remove('test.txt')
except FileNotFoundError as e:
    print(e)