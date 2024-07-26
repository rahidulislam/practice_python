class Cat:
    def __init__(self, color, action):
        self.color = color
        self.action = action

    def view(self):
        print(self.color, " cat is ", self.action)

    def compare(self, ct):
        # we receive object reference
        if self.action == ct.action:
            print("Both cate are ", self.action)
        else:
            print("They are different")


# ---------------------------------------------------
# object creation
c1 = Cat("white", "jumping")
c2 = Cat("Brown", "jumping")
c1.view()
c2.view()
c1.compare(c2) # passed by reference
