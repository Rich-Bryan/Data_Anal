#
# PaintJobEstimator.py
#
# A painting company has determined that for every 112 square feet of wall space, 
# one gallon of paint and eight hours of labor will be required. The company 
# charges $35.00 per hour for labor. 
#
# Write a program that asks the user to enter the square feet of wall space to be 
# painted and the price of the paint per gallon. 
#
# The program should display the following data:
#
#    The number of gallons of paint required
#    The hours of labor required
#    The cost of the paint
#    The labor charges
#    The total cost of the paint job
#
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
# Create a function called calculateNumberOfGallonsOfPaint.  This function will be passed the number of square 
# feet to be painted and will return the number of gallons of paint that will be needed:
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def calculateNumberOfGallonsOfPaint(squareFeet):
        # A painting company has determined that for every 112 square feet of wall space, 
        # one gallon of paint and eight hours of labor will be required. The company 
        # charges $35.00 per hour for labor. 
        gallons = squareFeet / 112
        return gallons//1
        

	


#
# Create a function called calculateHoursOfLabor here.  This function will be passed the number of square    
# feet to be painted and will return the number of hours it will take to paint this many square feet:
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def calculateHoursOfLabor(squareFeet):
        gallons = calculateNumberOfGallonsOfPaint(squareFeet)
        return gallons * 8
	
	
#
# Create a function called calculateCostOfPaint.  This function will be passed the number of gallons of paint 
# needed and the cost per gallon and will return the cost for this many gallons of this paint:
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def calculateCostOfPaint(numberOfGallonsOfPaint, paintCostPerGallon):
        return numberOfGallonsOfPaint * paintCostPerGallon

	


#
# Create a function called calculateLaborCharges here.  This function will be passed the number of hours of    
# labor to do the job and will return the charges for that labor:
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def calculateLaborCharges(hoursOfLabor):
	return hoursOfLabor * 35
	


#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        squareFeet             = float(input("How many square feet need to be painted? "))
        paintCostPerGallon     = float(input("How much does a gallon of paint cost? "))

        numberOfGallonsOfPaint = calculateNumberOfGallonsOfPaint(squareFeet)
        hoursOfLabor           = calculateHoursOfLabor(squareFeet)
        costOfPaint            = calculateCostOfPaint(numberOfGallonsOfPaint, paintCostPerGallon)
        laborCharges           = calculateLaborCharges(hoursOfLabor)
        totalCost              = costOfPaint + laborCharges

        print("To paint " + str(squareFeet) +  " square feet, we will need " + str(numberOfGallonsOfPaint) + " gallons of paint which will cost $" + str(costOfPaint) + ". The job will take " + str(hoursOfLabor) + " hours to complete which will cost $" + str(laborCharges) + " in labor for a total of $" + str(totalCost))

main()
