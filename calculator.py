# Create a calculator that can do basic math operations like + , - , x and /.
def add(num1 , num2):
    return num1 + num2
def sub(num1 , num2):
    return num1 - num2
def mul(num1 , num2):
    return num1 * num2
def div(num1 , num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

num1 = float(input("Your first number: "))
num2 = float(input("Your second number: "))
op = input("Operation you want to make ( + , - , x , /): ")

if op == "+":
    print(add(num1 , num2))
elif op == "-":
    print(sub(num1 , num2))
elif op == "x":
    print(mul(num1 , num2))
elif op == "/":
    print(div(num1 , num2))
else:
    print("Invalid operation.")
