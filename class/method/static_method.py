class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 1.8 + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) / 1.8
    


print(Temperature.celsius_to_fahrenheit(25))
print(Temperature.fahrenheit_to_celsius(77))