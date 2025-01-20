class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 1.8 + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) / 1.8
    


print(Temperature.celsius_to_fahrenheit(25))
print(Temperature.fahrenheit_to_celsius(77))


class TemperatureConverter:
    KELVIN = 'K'
    FAHRENHEIT = 'F'
    CELSIUS = 'C'

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return 9*celsius/5 + 32
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273
    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return 5*(fahrenheit+459.67)/9
    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return 9*kelvin/5 - 459.67
    @staticmethod
    def format(value, unit):
        symbol = ''
        if unit == TemperatureConverter.KELVIN:
            symbol = 'K'
        elif unit == TemperatureConverter.FAHRENHEIT:
            symbol = 'F'
        elif unit == TemperatureConverter.CELSIUS:
            symbol = 'C'
        return f'{value}{symbol}'
    
F = TemperatureConverter.fahrenheit_to_celsius(77)
print(TemperatureConverter.format(F, TemperatureConverter.CELSIUS))