#
# DayOfWeek.py
#
# Write a program that asks the user for a number in the range of 1 through 7. The program should 
# display the corresponding day of the week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 
# 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should display an error message if the user 
# enters a number that is outside the range of 1 through 7.
#

user = int(input("Enter a number between 1 - 7: "))
if user == 1:
    print("Monday")

elif user == 2:
    print("Tuesday")

elif user == 3:
    print("Wednesday")

elif user == 4:
    print("Thrusday")

elif user == 5:
    print("Friday")

elif user == 6:
    print("Saturday")

elif user == 7:
    print("Sunday")

else:
    print("wrong number")