try:
    a="hello there"
    print(a)
except NameError:
    print("variable not defined")
else:
    print("variable defined")
# finally:
#     print("error handeling is done") 