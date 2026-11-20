from .calculator import Calculator

def main() -> float:
    print("Hello from simple calc-ex!")
    print("Choose calculation type:")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")

    selection = int(input("Select 1-4: "))
    x = float(input("Enter first nr: "))
    y = float(input("Enter second nr: "))

    if selection == 1:
        return Calculator.sum(x,y)
    elif selection == 2:
        return Calculator.sub(x,y)
    elif selection == 3:
        return Calculator.multiply(x,y)
    elif selection == 4:
        return Calculator.div(x,y)
    else: 
        raise TypeError("No such calculation available")
     
    