# write file
f = open("test.txt", "w")
f.write("Hello World")
f.close()

# read file
f = open("test.txt", "r")
print(f.read())
f.close()

# append file
f = open("test.txt", "a")
f.write("\nnew line here")
f.close()