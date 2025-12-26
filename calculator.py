"""
Simple Calculator Program
This calculator performs basic arithmetic operations.
WARNING: Contains a division by zero bug!
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    # BUG: No check for division by zero!
    return a / b

def calculate(operation, num1, num2):
    """Perform calculation based on operation"""
    if operation == "add":
        return add(num1, num2)
    elif operation == "subtract":
        return subtract(num1, num2)
    elif operation == "multiply":
        return multiply(num1, num2)
    elif operation == "divide":
        return divide(num1, num2)
    else:
        return "Invalid operation"

def main():
    """Main function to run the calculator"""
    print("Welcome to Simple Calculator!")
    print("Available operations: add, subtract, multiply, divide")
    print()
    
    operation = input("Enter operation: ").lower()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = calculate(operation, num1, num2)
    print(f"\nResult: {result}")

if __name__ == "__main__":
    print("Hello world!")
    main()