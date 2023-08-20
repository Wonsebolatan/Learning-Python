"""
print('Ibrahim Bashiru')
print('o----')
print(' ||||')
print('*' * 10)

#variable
price = 10   #integer variable type
price = 20
rating = 4.9  #float
name = 'Ibrahim'  #string
is_published = True  #boolean variable true or false
print(price)

#get input
name = input('What is your name? ')
print('Hi ' + name)

#type conversion
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2023 - int(birth_year)
print(type(age))
print(age)

# Arithmetic Operations
x = 10
x -= 3
print(x)

# Operator Precedence - orders is - parenthesis, exponentiation, multiplication or division and addition or subtraction
x = (10 + 3) * 2 ** 2
print(x)

# Math Functions
import math # needed for complex mathematics calculation
print(math.ceil(2.9))
print(math.floor(2.9))
x= 2.9
print(round(x))
print(abs(-2.9)) #absolute (abs()) function alway returns a popsitive result
"""

# if Statements
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")