#
# MilesPerGallon.py
#
# A car's miles-per-gallon (MPG) can be calculated with the following formula:
#
#    MPG=MilesDriven/GallonsOfGasUsed
#
# Write a program that asks the user for the number of miles driven and the gallons of gas used. It should 
# calculate the car's MPG and display the result.
#

numberOfMiles = float(input("Enter number of miles driven: "))
gallonOfGasUsed = float(input("Enter gallon of gas used: "))

MPG_car = numberOfMiles/gallonOfGasUsed

print("MPG", MPG_car)