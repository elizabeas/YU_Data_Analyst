print('This calculator accepts a first number, type of operation, and second number and calculates the result.')
num1 = float(input('Enter the first number: '))
opr = input('Type of operation (+, -, *, or /): ')
num2 = float(input('Enter the second number: '))

if opr == ('+'):
    print(num1 + num2)
elif opr == ('-'):
    print(num1 - num2)
elif opr == ('*'):
    print(num1 * num2)
elif opr == ('/'):
    print(num1 / num2)
else:
    print('Operation not recognized. Please try again.')