class MyIterator:
    def __init__(self,start,end):
        self.start = start
        self.end =end
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
        
my_iter = MyIterator(1,5)
for num in my_iter:
    print(num)

print(my_iter)

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

class CountDown:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        while self.start >0:
            yield self.start
            self.start -= 1
    
countdown = CountDown(5)
for num in countdown:
    print(num)