import multiprocessing
import time

def print_numbers():
    for i in range(1,6):
        print(i)
        time.sleep(1)

process = multiprocessing.Process(target=print_numbers)
process.start()

for i in range(1,6):
    print(f"Main Process: {i}")
    time.sleep(1)

process.join()
print("Both Process finished")