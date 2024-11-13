#
# TotalPurchases.py
#
# A customer in a store is purchasing five items. Write a program that asks for the price of each item, then displays 
# the subtotal of the sale, the amount of sales tax, and the total. Assume the sales tax is 7 percent.
#

item1 = int((input("Enter price for Item 1: ")))
item2 = int((input("Enter price for Item 2: ")))
item3 = int((input("Enter price for Item 3: ")))
item4 = int((input("Enter price for Item 4: ")))
item5 = int((input("Enter price for Item 5: ")))

subtotal = item1 + item2 + item3 + item4 + item5

total = subtotal * 0.07

print("Totoal is: " , total)