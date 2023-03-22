num1 = int(input("enter number 1: "))
op = input("enter operation (+, -, *, /): ")
num2 = int(input("enter number 2: "))

match op:
    case '+':
        print(f"{num1} + {num2} = {num1+num2}")
    case '-':
        print(f"{num1} - {num2} = {num1-num2}")
    case '*':
        print(f"{num1} * {num2} = {num1*num2}")
    case '/':
        print(f"{num1} / {num2} = {num1/num2}")
    case _:
        print("Invalid Operator")

