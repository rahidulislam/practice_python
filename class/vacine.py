class Vaccine:
    def __init__(self, name, made_in, interval):
        self.name = name
        self.made_in = made_in
        self.interval = interval


# ==================================================
class Person:
    def __init__(self, pname, age, ptype="General Citizen"):
        self.pname = pname
        self.age = age
        self.ptype = ptype
        self.vaccine = ""
        self.first_dose = False
        self.second_dose = False

    def push_vaccine(self, vaccine, dose="1st dose"):
        if dose == "1st dose":
            if self.age >= 25 or self.ptype == "Student":
                self.vaccine = vaccine
                self.first_dose = True
                print("first dose done for", self.pname)
            else:
                print("sorry", self.pname, "minimum age for taking vaccine is 25 years old")
        else:
            if self.vaccine.name != vaccine.name:
                print("Sorry", self.pname, "You can not take 2 different vaccine")
            elif self.first_dose:
                self.second_dose = True
                print("2nd dose done for", self.pname)

    def show_detail(self):
        print("Name:", self.pname, "Age:", self.age, "Type:", self.ptype)
        print("Vaccine Name:", self.vaccine.name)
        if self.first_dose and self.second_dose:
            print("1st dose given")
            print("2nd dose given")
        elif self.first_dose:
            print("1st dose given")
            print("2nd dose: please come after", self.vaccine.interval, "days")


# ================================================================================
astra = Vaccine("Astrazeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("=========================================================================")
p1.push_vaccine(astra)
p1.show_detail()
p1.push_vaccine(sin, "2nd dose")
p1.push_vaccine((astra, "2nd dose"))
print("=========================================================================")
p2 = Person("Carol", 23, "Actor")
p2.push_vaccine(sin)
print("=========================================================================")
p3 = Person("David", 34)
p3.push_vaccine(modr)
p3.show_detail()
p3.push_vaccine(modr, "2nd dose")
