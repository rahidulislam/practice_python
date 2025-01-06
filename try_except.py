try:
    print("Enter the net sales for")
    previous = float(input("Prior period: "))
    current = float(input("Current period: "))
    change = (current-previous)*100/previous
    if change>0:
        result = f"sales increase {abs(change)}"
    else:
        result = f"sales decrease {abs(change)}"
    print(result)
except ValueError:
    print("Error! Please enter a number for net sales.")
except ZeroDivisionError:
    print("Error! Cannot divide by zero.")
except Exception as e:
    print(e)
finally:
    print("Goodbye!")

def calculate_bmi(height, weight):
    """calculate body mass index"""
    return weight/height**2

def evaluate_bmi(bmi):
    if 18.5 <= bmi <=24.9:
        return "Normal"
    elif bmi < 18.5:
        return "Underweight"
    else:
        return "Overweight"
    
def main():
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))
    except ValueError:
        print("Error! Please enter a number for height and weight.")
    else:
        bmi = round(calculate_bmi(height, weight),1)
        evaluation = evaluate_bmi(bmi)
        print(f"Your BMI is {bmi} and you are {evaluation}")

if __name__ == "__main__":
    main()