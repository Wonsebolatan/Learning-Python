"""
Price of a house is $1M
IF buyer has good credit,
    they need to put down 10%
Otherwise
    they need to put down 20%
Print the down payment
"""

is_credit_good = True
cost_of_house = 1000000
if is_credit_good:
    down_payment = cost_of_house * 0.1
else:
    down_payment = cost_of_house * 0.2

print("$",down_payment)
print(f"Down payment: ${down_payment}") #this line was copied from instructor code.