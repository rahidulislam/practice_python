from contextlib import contextmanager
class MyContextManager:
    def __enter__(self):
        print("Enter the context and setting up resources.....")
        return self
    
    def __exit__(self, exc_type, exc_val,exc_tb):
        print("Exiting the context and Cleaning up resources.....")
        if exc_type:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            print(f"Exception trace: {exc_tb}")
        return False
    
with MyContextManager() as manager:
    print("Inside with block")
    print(f"Manager: {manager}")

@contextmanager
def my_context_manager():
    print("Enter the context....")
    yield
    print("Exit the context....")

with my_context_manager():
    print("Inside with context block")