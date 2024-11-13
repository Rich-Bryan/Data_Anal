#
# SalesTaxProgramRefactoring.py
#
# Programming Exercise #6 in Chapter 2 was the Sales Tax program. For that exercise, you 
# were asked to write a program that calculates and displays the county and state sales tax 
# on a purchase. If you have already written that program, redesign it so the subtasks are 
# in functions. If you have not already written that program, write it using functions.
# 
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the functions 
# that do the actual work and returns the results to the main program.

#
# Create a function called calculateStateSalesTax here.  This function will be passed the subtotal and will return
# the state sales tax on that subtotal:
#

def calculateStateSalesTax(subtotal):
        stateSaleTax = 0.05 

        return subtotal * stateSaleTax

	

#
# Create a function called calculateCountySalesTax here.  This function will be passed the subtotal and will return
# the county sales tax on that subtotal:
#

def calculateCountySalesTax(subtotal):
        countySalesTax = 0.025
        return subtotal * countySalesTax

	

#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        subtotal = float(input("What is the total of the order before sales tax? "))

        stateSalesTax = calculateStateSalesTax(subtotal)
        countySalesTax = calculateCountySalesTax(subtotal)

        print("The amount of the purchase is", subtotal)
        print("The state sales tax is" , stateSalesTax)
        print("The county sales tax is", countySalesTax)
        print("The order total with state and county sales tax is", subtotal+stateSalesTax+countySalesTax)

main()        
