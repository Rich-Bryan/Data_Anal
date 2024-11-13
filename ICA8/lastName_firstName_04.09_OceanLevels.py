#
# OceanLevels.py
#
# Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an application 
# that displays the number of millimeters that the ocean will have risen each year for the next 25 years.
#
# Your program must use a loop to display this information.  For example, your output should look something like: 
#
#   By year 1 the ocean will have risen 1.6 millimeters
#   By year 2 the ocean will have risen 3.2 millimeters
#   By year 3 the ocean will have risen 4.800000000000001 millimeters
#   By year 4 the ocean will have risen 6.4 millimeters
#   By year 5 the ocean will have risen 8.0 millimeters
#   By year 6 the ocean will have risen 9.600000000000001 millimeters
#   By year 7 the ocean will have risen 11.200000000000001 millimeters
#   By year 8 the ocean will have risen 12.8 millimeters
#   By year 9 the ocean will have risen 14.4 millimeters
#   By year 10 the ocean will have risen 16.0 millimeters
#   By year 11 the ocean will have risen 17.6 millimeters
#   By year 12 the ocean will have risen 19.200000000000003 millimeters
#   By year 13 the ocean will have risen 20.8 millimeters
#   By year 14 the ocean will have risen 22.400000000000002 millimeters
#   By year 15 the ocean will have risen 24.0 millimeters
#   By year 16 the ocean will have risen 25.6 millimeters
#   By year 17 the ocean will have risen 27.200000000000003 millimeters
#   By year 18 the ocean will have risen 28.8 millimeters
#   By year 19 the ocean will have risen 30.400000000000002 millimeters
#   By year 20 the ocean will have risen 32.0 millimeters
#   By year 21 the ocean will have risen 33.6 millimeters
#   By year 22 the ocean will have risen 35.2 millimeters
#   By year 23 the ocean will have risen 36.800000000000004 millimeters
#   By year 24 the ocean will have risen 38.400000000000006 millimeters
#   By year 25 the ocean will have risen 40.0 millimeters
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called displayOceanLevelRise.  This function will not be passed anything and will not return
# anything.  It will loop through the 25 years and show the 1.6 mm rise year after year:  
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def displayOceanLevelRise():
        oceanLevel = 1.6
        for i in range(25):
                print(f"By year 1 the ocean will have risen {oceanLevel*(i+1)} millimeters")


	

#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        displayOceanLevelRise()

main()
