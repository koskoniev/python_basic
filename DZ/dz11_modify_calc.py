run = True
while run:
    num1 = int(input("Enter 1st number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = int(input("Enter 2st number: "))
    result = None

    if ((type(num1) is int) or (type(num1) is float)) and ((type(num2) is int) or (type(num2) is float)):  # check data type
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error. Divisor cannot be 0")
                num2 = float(input("Enter 2st number again: "))
            result = num1 / num2
        else:
            print("Unknown action")
        print(num1, operator, num2, "=", result)
    else:
        print("Type is not 'int' or 'float'", "\n", "BYE")

    again = True
    while again:
        run_again = (input("Run again? (Y/N): ")).strip().lower()
        if run_again == 'y':
            run = True
            again = False
        elif run_again == 'n':
            print('Bye:)')
            run = False
            again = False
        else:
            print('Incorrect input. Must be \'y\' or \'n\'.')
            run = False
            again = True
