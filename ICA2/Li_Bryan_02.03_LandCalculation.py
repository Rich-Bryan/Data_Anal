#
# LandCalculation.py
#
# One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to enter the total square feet 
# in a tract of land and calculates the number of acres in the tract.
#
# Hint: Divide the amount entered by 43,560 to get the number of acres.
#

squareFeet = float(input("Enter total square feet: "))
total = squareFeet/43560

print(total)
