#
# KilometerConverter.py
#
# Write a program that asks the user to enter a distance in kilometers, then converts that distance to miles. 
#
# The conversion formula is as follows:
#
#    miles = kilometers * 0.6214
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.

#
# Create a function called kilometersToMiles here.  This function will be passed the number of kilometers and will
# return the equivelant distance in miles:
#

def kilometersToMiles(kilometers):
        miles = kilometers * 0.6214
        return miles

#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        kilometers = float(input("How many kilometers? "))
        miles = kilometersToMiles(kilometers)
        print(kilometers, "kilometers is equal to", miles, "miles.")

main()
