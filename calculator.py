# Ask the user to input the first number
num1 = float(input("Enter the first number: "))

# Ask the user to input the second number
num2 = float(input("Enter the second number: "))

# Ask the user to input the operator
operator = input("Enter the operator (+, -, *, /):")

# Perform the operation
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)

# Check for division by zero
elif operator == "/" and num2 != 0:
    print(num1 / num2)
else:
    print("Error: Division by zero is not allowed.")

