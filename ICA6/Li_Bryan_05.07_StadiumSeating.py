#
# StadiumSeating.py
#
# There are three seating categories at a stadium. Class A seats cost $20, Class B seats 
# cost $15, and Class C seats cost $10. 
#
# Write a program that asks how many tickets for each class of seats were sold, then displays 
# the amount of income generated from ticket sales.
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.

#
# Create a function called calculateIncomeFromTicketSales.  This function will be passed the class A, class B and class C
# thckets sold and will return the income generated by ticket sales. 
#
# The value returned needs to be a number, either a floating point number or an integer, not a string that may 
# include characters like the dollar character ("$") or the comma (",") used as a thousands separator.
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def calculateIncomeFromTicketSales(classATickets, classBTickets, classCTickets):
        #There are three seating categories at a stadium. Class A seats cost $20, Class B seats 
        # cost $15, and Class C seats cost $10. 
        income = (classATickets*20) + (classBTickets*15) + (classCTickets*10)
        return income


	

#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        classATickets = int(input("How many class A tickets have been sold? "))
        classBTickets = int(input("How many class B tickets have been sold? "))
        classCTickets = int(input("How many class C tickets have been sold? "))

        incomeFromTicketSales = calculateIncomeFromTicketSales(classATickets, classBTickets, classCTickets)

        print("The income generated from ticket sales was $" + str(incomeFromTicketSales))

main()
