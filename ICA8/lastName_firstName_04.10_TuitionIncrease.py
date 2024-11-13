#
# TuitionIncrease.py
#
# At one college, the tuition for a full-time student is $8,000 per semester. It has been announced that 
# the tuition will increase by 3 percent each year for the next 5 years. Write a program with a loop that 
# displays the projected semester tuition amount for the next 5 years.
#
# Your program must use a loop to display this information.  For example, your output should look something like: 
#
#    Starting at $8000 and rising at 3% per year, after 1 year(s) tuition cost will be $8240.0
#    Starting at $8000 and rising at 3% per year, after 2 year(s) tuition cost will be $8487.2
#    Starting at $8000 and rising at 3% per year, after 3 year(s) tuition cost will be $8741.816
#    Starting at $8000 and rising at 3% per year, after 4 year(s) tuition cost will be $9004.07048
#    Starting at $8000 and rising at 3% per year, after 5 year(s) tuition cost will be $9274.192594400001
#    At the end of the 5 year period, tuition will cost 9274.192594400001
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called displaytTuitionCost.  This function will not be passed anything.  The function will 
# return the cost of tuition at the end of the five year period.  The function will also show the cost of 
# tuition for each year of the 5 year period:  
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def displaytTuitionCost():
        tuition = 8000
        yearlyIncrease = 0.03
        for i in range(5):

                tuition += (tuition*yearlyIncrease)
                print(f"Starting at $8000 and rising at 3% per year, after {i+1} year(s) tuition cost will be ${tuition}")

	

#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        tuitionCostAfterFiveYears = displaytTuitionCost()
        print("At the end of the 5 year period, tuition will cost", tuitionCostAfterFiveYears)

main()
