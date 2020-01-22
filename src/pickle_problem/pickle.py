"""
You are tasked with calculating the price and number of ingredients for a pickle sandwich shop based on a number of customers.
!Every third customer will order a jumbo pickle sandwich while all others will order a regular pickle sandwich.
Your program should calculate the ingredients used as follows:
!Regular Pickle Sandwich = 1 Pickle and 2 Bread
!Jumbo Pickle Sandwich = 2 Pickle and 3 Bread
Your program will be provided input on multiple lines containing the number of customers, the price of pickle ingredients and the price of bread ingredients.
Your program should output the number of pickle ingredients used, the number of bread ingredients used and the combined price of all used ingredients.
Your program should handle invalid input and return the output of 'ERROR' in this scenario.
You are encouraged to use reference material from the internet to help you complete this challenge.
Please see the example input and output below.
Example  input:
50
0.75
0.50
output:
Pickle Quantity: 66
Bread Quantity: 116
Ingredient Cost: $107.50
Example
input: 0
output: ERROR
"""
customer_count = int(input("Enter number of customers:\n" ))
pickle_cost = float(input("Enter price of pickles:\n"))
bread_cost = float(input("Enter price of bread:\n"))


def solution(customer, pickle, bread):
    if customer  < 0:
        print("ERROR")
    else:
        jumbo = customer  // 3
        regular = customer - jumbo
        jumbo_cost = (3 * bread) + (2 * pickle)
        regular_cost = (2 * bread) + (1 * pickle)
        total = (jumbo * jumbo_cost) + (regular * regular_cost)
    return round(total, 2)


print(f"\n\nTotal cost for {customer_count} customers \n$", solution(customer_count, pickle_cost, bread_cost))
