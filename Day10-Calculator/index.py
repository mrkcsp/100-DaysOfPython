

def calculate(num1, operation, num2):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        return a / b
    
    operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,    
    }

    return operations[operation](num1, num2)
    
    


memory = 0
more = True

while more:
    if memory == 0:
        first_number = float(input("What's the first number?  "))
    operator = input("+\n-\n*\n/\nPick an operation:  ")
    second_number = float(input("What's the next number?  "))
    
    if memory == 0:
        completed_op = calculate(first_number, operator, second_number)
    else: 
        completed_op = calculate(memory, operator, second_number)

    user_choice = input(f"'y' to continue calculating with {completed_op} or 'n' to start a new one? Else to exit 'e' \n")

    if user_choice.lower() == "y":
        memory = completed_op
    elif user_choice.lower() == "n":
        memory = 0
    else:
        more = False
 


     