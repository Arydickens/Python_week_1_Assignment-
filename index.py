# Basic Calculator Program
print("To Perform the operation, please enter two numbers")
number1 = int(input("Enter the first Number: "))
number2 = int(input("Enter the second number: "))

operation = input(
    "Enter an operation (+ for addition, - for subtraction, * for multiplication, / for division): ")

if operation == "+":
    Ans = number1 + number2
    print(number1, "+", number2, "=", Ans)
elif operation == "-":
    Ans = number1 - number2
    print(number1, "-", number2, "=", Ans)
elif operation == "*":
    Ans = number1 * number2
    print(number1, "*", number2, "=", Ans)
elif operation == "/":
    Ans = number1/number2
    print(number1, "/", number2, "=", Ans)
else:
    print("Ivalid Operation")
