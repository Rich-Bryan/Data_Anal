#
# TipTaxTotal.py
#
# Write a program that calculates the total amount of a meal purchased at a restaurant. The program 
# should ask the user to enter the charge for the food, then calculate the amounts of a 18 percent tip 
# and 7 percent sales tax. Display each of these amounts and the total.
#

mealTotal = float((input("Enter the meal purchased at a restaurant: ")))
tip_percent = mealTotal * 0.18
sale_tax = mealTotal*0.07 

total = mealTotal + tip_percent + sale_tax

print("Cost of meal:", mealTotal, "tip:", tip_percent, "sale tax:", sale_tax)
print("Total:", total)
