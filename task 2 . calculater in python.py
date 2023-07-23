def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = int(input("Enter choice (1/2/3/4): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice in (1, 2, 3, 4):
            break
        else:
            print("Invalid choice. Please select a valid operation.")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    else:
        result = divide(num1, num2)

    print("Result: ", result)

if __name__ == "__main__":
    calculator()
