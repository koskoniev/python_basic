print("DZ4: Calc")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2st number: "))
operator = input("Enter operator (+, -, *, /): ")
result = None

# тут просто пробую сложные конструкции для проверки работы and/or
if ((type(num1) is int) or (type(num1) is float)) and ((type(num2) is int) or (type(num2) is float)):  # check data type
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            # если делитель 0, то просим ввести новое число
            print("Error. Divisor cannot be 0")
            num2 = float(input("Enter 2st number again: "))
        result = num1 / num2
    else:
        # если оператор не ( +, -, *, / )
        print("Unknown action")
    print(num1, operator, num2, "=", result)
else:
    # ну тут так... "иф должен быть закрыт элсом"
    print("Type is not 'int' or 'float'", "\n", "BYE")
