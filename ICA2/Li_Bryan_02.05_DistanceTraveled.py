#
# DistanceTraveled.py
#
# Assuming there are no accidents or delays, the distance that a car travels down the interstate can be calculated 
# with the following formula:
#
#    Distance=Speed×Time
#
# Write a program that prompts the user for the speed that a car is traveling and
# prompts the user for the amount of time the car has been traveling.  The program
# will then display the distance traveled in that time at that speed.
#

speed = float(input("Enter the speed that car is traveling: "))
time = float(input("Enter the time the car has been traveling: "))
distance = speed * time

print(distance)