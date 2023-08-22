weight = input('Weight: ')
weight_type = input('(L)bs or (K)g: ')

if weight_type.lower() == 'k':
    print(f" You are {round(int(weight)/ 0.45)} pounds")
elif weight_type.lower() == 'l':
    print(f" You are {round(int(weight) *0.45)} kilograms")


"""
Instructor solution 

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() =='L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
"""


