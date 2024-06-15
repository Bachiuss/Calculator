import logo
print(logo.logo)

def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiply,
    "/":divide
}

def calculator():
    number1 = float(input("Type first number: "))
    for i in operations:
        print(i)
    should_continue = True

    while should_continue:
        pick_symbol = input("Pick an operation: ")
        number2 = float(input("Type second number: "))
        calculation_function = operations[pick_symbol]
        ans = calculation_function(number1, number2)

        print(f"{number1} {pick_symbol} {number2} = {ans}")

        if input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start again ").lower() == "y":
            number1 = ans
        else:
            should_continue = False
            calculator()

calculator()