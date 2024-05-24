class BMI:
    KILOGRAMS_PER_POUND = 0.45359237
    METERS_PER_INCH = 0.0254

    def _init_(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height * BMI.METERS_PER_INCH

    def get_bmi(self):
        return (self.weight * BMI.KILOGRAMS_PER_POUND) / (self.height ** 2)

    def get_status(self):
        bmi_data = self.get_bmi()

        if bmi_data < 18.5:
            return "Underweight"
        elif bmi_data < 25:
            return "Normal"
        else:
            return "Overweight"

    def get_name(self):
        return self.name


if __name__ == "__main__":
    bmi = BMI("Tanvir Rifat", 145, 70)
    print(f"The BMI for {bmi.get_name()} is ({bmi.get_bmi():.2f}) {bmi.get_status()}")