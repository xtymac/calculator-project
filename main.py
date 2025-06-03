from multiprocessing.connection import answer_challenge


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO: Use the dictionary operations to perform the calculations.

def calculator():
    number1 = float(input("What is your first number? "))

    while True:
        for symbol in operations:
            print(symbol)

        user_input = input("Pick an operation: ")

        if user_input in operations:
            number2 = float(input("What is your second number? "))
            operation = operations[user_input]
            result = operation(number1, number2)
            print(f"{number1} {user_input} {number2} = {result}")

            choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
            if choice == "y":
                number1 = result
            else:
                print("\n" * 20)
                calculator()
                break
        else:
            print("Sorry, that's not a valid input.")

calculator()