"""Add appropriate commenting and documentation for the code below."""

# Adds two numbers
def add(x, y):
    return x + y

# Subtracts two numbers
def subtract(x, y):
    return x - y

# Multiplies two numbers
def multiply(x, y):
    return x * y

# Divides a number by another number
def divide(x, y):
    return x / y

# User interface
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:  # Infinite loop until the user provides an input
    # Prompts for user input
    choice = input("Enter choice(1/2/3/4): ")

    # Checks the userinput
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # Checks if the user wants to make another calculation
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
        else:
            print("Invalid Input")