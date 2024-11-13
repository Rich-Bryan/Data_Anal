#
# MagicDates.py
#
# The date June 10, 1960, is special because when it is written in the following format, the month 
# times the day equals the year:
#
#    6/10/60
#
# Design a program that asks the user to enter a month (in numeric form), a day, and a two-digit year. 
# The program should then determine whether the month times the day equals the year. If so, it should 
# display a message saying the date is magic. Otherwise, it should display a message saying the date 
# is not magic.
#


month = int(input("Enter the month (numeric form): "))
day = int(input("Enter the day: "))
year = int(input("Enter the two-digit year: "))


if month < 1 or month > 12:
    print("Invalid month. It should be between 1 and 12.")
if day < 1 or day > 31:  
    print("Invalid day. It should be between 1 and 31.")
if year < 0 or year > 99:
    print("Invalid year. It should be a two-digit number.")

if month * day == year:
    print("The date is magic!")
else:
    print("The date is not magic.")