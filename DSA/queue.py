from collections import deque
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"
    
    def size(self):
        return len(self.queue)
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
print(q.front())
print(q.is_empty())
print(q.size())
#==========================================
class Queue1:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.popleft() if self.queue else "Queue is empty"
    
    def front(self):
        return self.queue[0] if self.queue else "Queue is empty"
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
q1 = Queue1()
q1.enqueue(10)
q1.enqueue(20)
print(q1.dequeue())
print(q1.front())
print(q1.is_empty())    
print(q1.size())
#==========================================
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue2:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data):
        new_node = Node(data)
        if not self.front:
            self.front = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_data
    
    def front_value(self):
        return self.front.data if self.front else "Queue is empty"
    
    def is_empty(self):
        return self.front is None
    
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()
        
q2 = Queue2()
q2.enqueue(10)
q2.enqueue(20)
q2.enqueue(30)
print(q2.dequeue())
print(q2.front_value())
print(q2.is_empty())
q2.display()
        