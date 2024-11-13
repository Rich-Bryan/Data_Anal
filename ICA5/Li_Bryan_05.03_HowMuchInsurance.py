#
# HowMuchInsurance.py
#
# Many financial experts advise that property owners should insure their homes or buildings for 
# at least 80 percent of the amount it would cost to replace the structure. Write a program that 
# asks the user to enter the replacement cost of a building, then displays the minimum amount of 
# insurance he or she should buy for the property.
#
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.

#
# Create a function called calculateNeededInsurance here.  This function will be passed the replacement cost of a 
# building and will return the amount of insurance that should be purchased:
#

def calculateNeededInsurance(replacementCost):
        insuranceCost = replacementCost * 0.80
        return insuranceCost
       

	

#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        replacementCost = float(input("What is the replacement cost for the building? "))
        neededInsurance = calculateNeededInsurance(replacementCost)
        print("You will need", neededInsurance, "in insurance to cover a building with a replacement cost of", replacementCost)

main()
