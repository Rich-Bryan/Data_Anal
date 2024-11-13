#
# MassAndWeight.py
#
# Scientists measure an object’s mass in kilograms and its weight in newtons. If you know the amount 
# of mass of an object in kilograms, you can calculate its weight in newtons with the following formula:
#
#    weight=mass×9.8
#
# Write a program that asks the user to enter an object’s mass, then calculates and displays its weight. 
#
# If the object weighs more than 500 newtons, also display a message indicating that it is too heavy. 
#
# If the object weighs less than 100 newtons, also display a message indicating that it is too light.
#

mass = float(input("Enter Mass for object: "))

formula_wieght = mass*9.8

print("Weight: ", formula_wieght)

if formula_wieght > 500:
    print("too heavy")

elif formula_wieght < 100:
    print("too light")

else:
    print("good weight")