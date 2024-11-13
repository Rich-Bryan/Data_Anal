#
# HotDogCookoutCalculator.py
#
# Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a program 
# that calculates the number of packages of hot dogs and the number of packages of hot dog buns 
# needed for a cookout, with the minimum amount of leftovers. The program should ask the user for 
# the number of people attending the cookout and the number of hot dogs each person will be given. 
#
# The program should display the following details:
#
#    The minimum number of packages of hot dogs required
#    The minimum number of packages of hot dog buns required
#    The number of hot dogs that will be left over
#    The number of hot dog buns that will be left over
#

import math

HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

number_of_people = int(input("Enter the number of people attending the cookout: "))
hot_dogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

# Total hot dogs needed
total_hot_dogs_needed = number_of_people * hot_dogs_per_person

# Calculate packages and leftovers for hot dogs
packages_of_hot_dogs = math.ceil(total_hot_dogs_needed / HOT_DOGS_PER_PACKAGE)
total_hot_dogs_provided = packages_of_hot_dogs * HOT_DOGS_PER_PACKAGE
leftover_hot_dogs = total_hot_dogs_provided - total_hot_dogs_needed


# Calculate packages and leftovers for buns
# Assuming 1 bun per hot dog
total_buns_needed = total_hot_dogs_needed
packages_of_buns = math.ceil(total_buns_needed / BUNS_PER_PACKAGE)
total_buns_provided = packages_of_buns * BUNS_PER_PACKAGE
leftover_buns = total_buns_provided - total_buns_needed


print(f"Minimum number of packages of hot dogs required: {packages_of_hot_dogs}")
print(f"Minimum number of packages of hot dog buns required: {packages_of_buns}")
print(f"Number of hot dogs left over: {leftover_hot_dogs}")
print(f"Number of hot dog buns left over: {leftover_buns}")
