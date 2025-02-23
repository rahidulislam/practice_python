from collections import deque
# Stack using list
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    

s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.peek())
print(s.is_empty())
print(s.size())

#==========================================
# stack using deque
class Stack1:
    def __init__(self):
        self.stack = deque()

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"
    
    def peek(self):
        return self.stack[-1] if self.stack else "Stack is empty"
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    

s1 = Stack1()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.pop())
print(s1.peek())
print(s1.is_empty())
print(s1.size())
#==========================================
# stack using linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack2:
    def __init__(self):
        self.top = None

    def push(self,item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return "Stack is empty"
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data
    
    def peek(self):
        if not self.top:
            return "Stack is empty"
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print("None")

s2 = Stack2()
s2.push(10)
s2.push(20)
s2.push(30)
print(s2.pop())
print(s2.peek())
print(s2.is_empty())
s2.display()
#==========================================
