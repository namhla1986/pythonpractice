greeting = input("What is your name? ")
num1 = float(input("Hello " + greeting + "," +  "please enter a number: "))
op = input("Please enter an operator: ")
num2 = float(input("Please enter a second number: "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Please choose a different operator")