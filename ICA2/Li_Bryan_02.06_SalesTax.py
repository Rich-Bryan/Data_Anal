#
# SalesTax.py
#
# Write a program that will ask the user to enter the amount of a purchase. The program should then compute 
# the state and county sales tax. Assume the state sales tax is 5 percent and the county sales tax is 2.5 percent. 
# The program should display the amount of the purchase, the state sales tax, the county sales tax, the total 
# sales tax, and the total of the sale (which is the sum of the amount of purchase plus the total sales tax).
#
# Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.
#


amountOfPurchase = float(input("Enter amount of purchase: "))
stateSaleTax = 0.05 
countySalesTax = 0.025

totalStateSaleTax = amountOfPurchase * stateSaleTax
totalCountySaleTax = amountOfPurchase * countySalesTax
totalSaleTax = totalStateSaleTax + totalCountySaleTax

totalSale = amountOfPurchase+totalSaleTax

print("Amount purchase: ", amountOfPurchase, " State Sale Tax: ", stateSaleTax*100, "County Sale Tax: ", countySalesTax*100, " Total Sales Tax: ", totalSaleTax, " Total Sale: ",totalSale )



