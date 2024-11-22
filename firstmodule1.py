# import first module
import firstmodule
# import builtin module
import random
import platform

print(firstmodule.sayHi("Rahidul"))
x = firstmodule.player1['age']
print(f"my age is {x}")

print(random.randint(1,100))
y = platform.release()
print(y)
print(dir(platform))
