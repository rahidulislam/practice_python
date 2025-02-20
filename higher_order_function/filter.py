scores = [70,60,80,90,50,45,65,79,83]
# filtered =[]
# for score in scores:
#     if score >= 70:
#         filtered.append(score)
# print(filtered)

filtered = filter(lambda score: score >=70,scores)
print(list(filtered))

# countries with population greater than 300 million
countries = [
    ['China', 1394015977],
    ['India', 1339180127],
    ['USA', 329494365],
    ['Indonesia', 267625568],
    ['Brazil', 210147125],
    ['Pakistan', 205796555],
    ['Nigeria', 200962417],
    ['Bangladesh', 168065920],
    ['Russia', 143895551],
    ['Mexico', 132328035]
]
populated = filter(lambda country: country[1]>300000000, countries)
print(list(populated))

# even numbers
nums = [1,2,3,4,5,6,7,8,9,10]
even = filter(lambda num:num%2==0,nums)
print(list(even))

# Filter strings starting with a specific letter
words = ['apple','banana','cherry','date','elderberry','fig','grape','apricot']
filtered_words = filter(lambda word: word.startswith('a'),words)

print(list(filtered_words))

# Filter strings with length greater than 5
words = ['apple','banana','cherry','date','elderberry','fig','grape','apricot']
filtered_words = filter(lambda word: len(word)>5, words)
print(list(filtered_words))

# filter positive numbers
nums = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
positive  = filter(lambda num: num>0, nums)
print(list(positive))

# filter palindromes
words = ['madam', 'racecar', 'hello', 'world', 'level']
palindromes = filter(lambda word: word == word[::-1], words)
print(list(palindromes))

# filter prime numbers
nums = [1,2,3,4,5,6,7,8,9,10]
primes = filter(lambda num: num>1 and all(num%i!=0 for i in range(2,num)), nums)
print(list(primes))

# filter dictionaries by key value
nums = [{ 'a': 5 }, { 'a': 15 }, { 'a': 8 }]
filtered_nums  = filter(lambda num: num['a']<10, nums)
print(list(filtered_nums))

# filter vowels from a string
# vowels = 'aeiou'
sentence = 'hello world'
filtered_vowels = filter(lambda char: char in 'aeiou', sentence)
print(list(filtered_vowels))

# filter even length words
words = ['python', 'is', 'fun', 'and', 'educational']
even_length_words = filter(lambda word: len(word)%2==0, words)
print(list(even_length_words))

# filter valid email address
emails =['test@gmail.com', 'invalidemail', 'hello@domain.com', 'noatsign']
valid_emails = filter(lambda email: '@' in email and '.' in email, emails)
print(list(valid_emails))

# filter nested elemements
elements =[[1, 2, 3], [11, 12, 13], [4, 5, 6], [20, 30, 40]]
filtered_elements = filter(lambda element: all(num>10 for num in element), elements)
print(list(filtered_elements))