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