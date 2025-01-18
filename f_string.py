first_name ='john'
last_name = 'doe'
print(f'Hello {first_name} {last_name}')

website='pythontutorial.net'
message = (
    f'hello {first_name} {last_name}.\n'
    f'you are learning python at {website}'
)
print(message)
s=f'{1+2}'
print(s)

def inc(numbers,value):
    numbers[0] += value
    return numbers[0]
numbers = [0]
s = f'{inc(numbers,1)}, {inc(numbers,2)}, {inc(numbers,3)}'
print(s)

# format number using f-string
number = 400000000000
s = f'{number:,}'
print(s)