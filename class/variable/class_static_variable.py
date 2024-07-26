class Player:
    total_run = 0  # class or static variable which share among objects

    def __init__(self, name):
        self.name = name  # instance variable
        self.run = 0  # instance variable

    def hit_four(self):
        self.run += 4
        Player.total_run += 4

    def hit_six(self):
        self.run += 6
        Player.total_run += 6

    def show_run(self):
        print("Name:", self.name, "Run:", self.run, "Team Run:", Player.total_run)


# ======================================
sakib = Player("Sakib")
tamim = Player("Tamim")
sakib.hit_four()
sakib.show_run()
tamim.hit_six()
tamim.show_run()
sakib.hit_six()
sakib.show_run()
print(sakib.__dict__)
print(tamim.__dict__)
print(tamim.total_run)
