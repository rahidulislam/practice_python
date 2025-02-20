numbers  = [1,2,3,4,5,6,7,8,9,10]
even  = filter(lambda num: num%2==0, numbers)
print(list(even))

words = ["apple", "banana", "cherry", "date", "elderberry"]
result = filter(lambda word: len(word) >= 5, words)
print(list(result))