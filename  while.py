# i = 1
# while (i<=100):
#     if(i%4==0 and i%5==0):
#         print(i)
#     i = i+1

num = int(input("Enter a number: "))
count=0
while (num>0):
    count += 1
    num = num // 10
print("Total character of given number is: ",count)
