def calculator(x,y): #defining the function as calculator
    if i == 1:
        return x+y
    if i == 2:
        return x-y
    if i == 3:
        return x*y
    if i == 4:
        return x//y
    if i == 5:
        return x%y
    if i == 6:
        return x**y
print('Press 1 for Addition\n' 'Press 2 for Substraction\n' 'Press 3 for Multiplication\n' 'Press 4 for Division\n' 'Press 5 for Modulus\n'
'Press 6 for Exponent\n')
i = int(input('Enter the operation number: ')) #taking the input for operation
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
print(calculator(n1,n2))
