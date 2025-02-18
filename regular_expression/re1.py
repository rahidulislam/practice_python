import re
text = "Python is a programming language that lets you work quickly and integrate systems more effectively."
match = re.search(r'Python',text)
if match:
    print("Match found",match.group())
else:
    print("Match not found")

# findall
text = "The numbers are 45,78,100 and 200"
match = re.findall(r"\d+",text)
print(match)

#sub (replace text)
text = "I love Python! Python is amazing"
nex_text = re.sub(r"Python","Django",text)
print(nex_text)

#split text
text = "apple,banana;grapes orange"
words = re.split(r"[ ,;]",text)
print(words)

# Email Validation
email ="_test.email@example.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
if re.match(pattern,email):
    print("Valid email")
else:
    print("Invalid email")
