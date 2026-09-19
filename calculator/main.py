import art

print(art.logo)

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
    "/": divide,
}




def calculator():
    f_number = int(input("What is the first number? "))
    keep_going = True
    while keep_going is True:
        option = input("Choose an operation: ")
        for symbol in operations:
            print(symbol)
        s_number = int(input("What is the second number? "))


        total = (operations[option](f_number,s_number))

        print(f"{f_number} {option} {s_number} = {total} ")
        yes_or_no = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ")
        if yes_or_no == "y":
            keep_going = True
            f_number = total
        elif yes_or_no == "n":
            yes_or_no = False
            print("\n" * 20)
            calculator()


calculator()