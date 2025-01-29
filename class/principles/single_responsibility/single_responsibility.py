class Person:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Person(name={self.name})"
    
    # @classmethod
    # def save(cls,person):
    #     print(f"Save the {person} to the database")


class PersonDB:
    def save(self,person):
        print(f"Save the {person} to the database")

if __name__ == '__main__':
    p = Person("John")
    # print(p)
    # Person.save(p)
    db = PersonDB()
    db.save(p)
