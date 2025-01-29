# Single Responsibility Principle with Facade Pattern
class PersonDB:
    def save(self,person):
        print(f"Save the {person} to the database")

class Person:
    def __init__(self,name):
        self.name = name
        self.db = PersonDB()

    def __repr__(self):
        return f"Person(name={self.name})"
    
    def save(self):
        self.db.save(self)

if __name__ == '__main__':
    p = Person("John")
    p.save()