#
# PropertyTax.py
#
# A county collects property taxes on the assessment value of property, which is 60 percent 
# of the property’s actual value. For example, if an acre of land is valued at $10,000, its 
# assessment value is $6,000. The property tax is then 72¢ for each $100 of the assessment 
# value. The tax for the acre assessed at $6,000 will be $43.20. 
#
# Write a program that asks for the actual value of a piece of property and displays the 
# assessment value and property tax.
#
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.

#
# Create a function called calculateAssessedValue.  This function will be passed the actual value of a piece  
# of property and will return the assessed value (60%) of the actual value:
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def calculateAssessedValue(actualValue):
        return actualValue * 0.60

	


#
# Create a function called calculatePropertyTax here.  This function will be passed the assessed value of a piece  
# of property and will return the tax on that property (72¢ for each $100):
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def calculatePropertyTax(assessedValue):
        each_100 = 100  # Each $100
        tax_rate_per_100 = 0.72  # 72 cents for every $100
        tax = (assessedValue / each_100) * tax_rate_per_100
        return tax//1
	
	

#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        actualValue = float(input("What is the actual value of the property? "))
        assessedValue = calculateAssessedValue(actualValue)
        propertyTax = calculatePropertyTax(assessedValue)

        print("On a property with an actual value of", actualValue, "the property will be assessed for", assessedValue, "and you will pay a property tax of", propertyTax)

main()
