import os

try:
    os.rename('test.txt', 'test1.txt')
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)