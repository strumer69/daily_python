def calculator():
    print('Welcome to the Calculator!')
    print('You can perform basic arithmetic operations: +, -, *, /')

    num1 = float(input('Enter the first number: '))
    op = input('Enter the operation (+, -, *, /): ')
    num2 = float(input('Enter the second number: '))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            return 'Error: Division by zero is not allowed.'
        result = num1 / num2
    else:
        return 'Error: Invalid operation.'
    return f'The result of {num1} {op} {num2} is: {result}'
if __name__ == '__main__':
    print(calculator())
    