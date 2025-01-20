class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current
    
    def reset(self):
        self.__current = 0

counter = Counter()
counter.increment()
counter.increment()
counter.current = -999
counter.increment()
print(counter.value())
print(counter.__dict__)
print(counter._Counter__current)