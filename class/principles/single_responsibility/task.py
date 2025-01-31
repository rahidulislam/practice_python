# without SRP
class Task:
    def __init__(self, name:str, description:str):
        self.name = name
        self.description = description
        self.status = "Pending"

    def mark_as_completed(self):
        self.status = "Completed"

    def delete_task(self):
        print(f"Task {self.name} is deleted")

    def display_task_info(self):
        print(f"Task: {self.name}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")

task = Task("Task 1", "This is task 1")
task.display_task_info()
task.mark_as_completed()
task.display_task_info()
task.delete_task()

# with SRP
class Task2:
    def __init__(self,name:str,description:str):
        self.name = name
        self.description = description
        self.status = "Pending"

class TaskManager:
    @staticmethod
    def mark_as_completed(task:Task2):
        task.status = "Completed"

    @staticmethod
    def delete_task(task:Task2):
        print(f"Task {task.name} is deleted")

class Task2Printer:
    @staticmethod
    def display_task_info(task:Task2):
        print(f"Task: {task.name}")
        print(f"Description: {task.description}")
        print(f"Status: {task.status}")

task2 = Task2("Task 2", "This is task 2")
Task2Printer.display_task_info(task2)
TaskManager.mark_as_completed(task2)
Task2Printer.display_task_info(task2)
TaskManager.delete_task(task2)