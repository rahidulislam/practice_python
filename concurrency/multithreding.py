import threading
import time

# function to run in thread
def print_numbers():
    for i in range(10):
        print(i)
        time.sleep(1)

# create thread
thread = threading.Thread(target=print_numbers)

# start thread
thread.start()

# Main Thread work
for i in range(1,10):
    print(f"Main Thread: {i}")
    time.sleep(1)

# wait for thread to finish
thread.join()
print("Boath Thread finished")

def task(name):
    for i in range(3):
        print(f"{name} is running {i}")
        time.sleep(1)
thread1 = threading.Thread(target=task, args=("Thread1",))
thread2 = threading.Thread(target=task,args=("Thread2",))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Both tasks finished")