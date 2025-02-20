import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(3)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())
    print("Both tasks completed")

asyncio.run(main())

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main2():
    print("Start")
    await say_hello()
    print("End")
asyncio.run(main2())