# Simple Calculator Program

# start with creating functions for simple math problems
def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b 
def divide(a, b): 
    return a / b

# next add print statements so user sees the options
print('Choose an Operator.')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

# have user choose a function
user_select = input('Choose a number(1/2/3/4): ')
# user enter numbers for math problem
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

#if statement for each option and display the problem
if user_select == '1': 
    print(num1, '+', num2, '=', add(num1, num2))
elif user_select == '2':
        print(num1, '-', num2, '=', subtract(num1, num2))
elif user_select == '3': 
         print(num1, '*', num2, '=', multiply(num1, num2))
elif user_select == '4': 
         print(num1, '/', num2, '=', divide(num1, num2))
else: 
      print('Invalid Input')