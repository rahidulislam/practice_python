from os.path import exists
from pathlib import Path
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

# File reading
# with open("test.txt","r",encoding="utf-8") as f:
    # contents = f.readlines()
    # print(lines)
    # print(f.readline())
    # print(f.readlines())
    # for line in lines:
    #     print(line)
    # print(contents)
    # [print(line.strip()) for line in contents]
    # for line in f:
    #     print(line.strip())

# file writing
lines = ["Readme","How to write text files in python","Python is a programming language"]
with open("test.txt","w") as f:
    # f.write("I am writing to a file")
    # for line in lines:
    #     f.write(line)
    #     f.write("\n")
    f.writelines('\n'.join(lines))

more_lines = ["","Java is a programming language", "C++ is a programming language"]
with open("test.txt","a") as f:
    f.writelines('\n'.join(more_lines))

utf8_lines = ["",'আমার নাম রাহিদুল ইসলাম']
with open("test.txt","a",encoding="utf-8") as f:
    f.write("\n".join(utf8_lines))


print(exists("test.txt"))
path = Path("test.txt")
print(path.is_file())
if path.is_file():
    print(f"the file {path} exists")
else:
    print(f"the file {path} does not exist")
