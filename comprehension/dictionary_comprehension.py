squares ={}
for i in range(5):
    squares[i] = i**2
print(squares)

# dictionary comprehension
squares = {i:i**2for i in range(5)}
print(squares)

squares = {i:i**2 for i in range(5) if i%2==0}
print(squares)

word_length = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(word_length)