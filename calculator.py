def select_operation(choice):
    if choice == '+':
        return 'addition'
    elif choice == '-':
        return 'subtraction'
    elif choice == '*':
        return 'multiplication'
    elif choice == '/':
        return 'division'
    elif choice == '^':
        return 'power'
    elif choice == '%':
        return 'remainder'
    elif choice == '#':
        return 'terminate'
    elif choice == '$':
        return 'reset'
    else:
        return 'invalid'

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    while True:
        print("Select operation:")
        print("1. Add      : + ")
        print("2. Subtract : - ")
        print("3. Multiply : * ")
        print("4. Divide   : / ")
        print("5. Power    : ^ ")
        print("6. Remainder: % ")
        print("7. Terminate: # ")
        print("8. Reset    : $ ")

        choice = input("Enter choice (+, -, *, /, ^, %, #, $): ")

        operation = select_operation(choice)

        if operation == 'terminate':
            print("Done. Terminating")
            break
        elif operation == 'reset':
            print("Resetting calculator")
            continue
        elif operation == 'invalid':
            print("Invalid choice. Please select a valid operation.")
            continue

        num1 = get_float_input("Enter first number: ")
        num2 = get_float_input("Enter second number: ")

        if operation == 'addition':
            result = num1 + num2
        elif operation == 'subtraction':
            result = num1 - num2
        elif operation == 'multiplication':
            result = num1 * num2
        elif operation == 'division':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        elif operation == 'power':
            result = num1 ** num2
        elif operation == 'remainder':
            result = num1 % num2

        print(f"Result: {num1} {choice} {num2} = {result}")
