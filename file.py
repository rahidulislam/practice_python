# # write file
# f = open("test.txt", "w")
# f.write("Hello World")
# f.close()

# # read file
# f = open("test.txt", "r")
# print(f.read())
# f.close()

# # append file
# f = open("test.txt", "a")
# f.write("\nnew line here")
# f.close()

with open("test.txt","r",encoding="utf-8") as f:
    # contents = f.readlines()
    # print(lines)
    # print(f.readline())
    # print(f.readlines())
    # for line in lines:
    #     print(line)
    # print(contents)
    # [print(line.strip()) for line in contents]
    for line in f:
        print(line.strip())