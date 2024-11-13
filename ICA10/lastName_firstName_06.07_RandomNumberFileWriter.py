#
# RandomNumberFileWriter.py
#
# Write a program that writes a series of random numbers to a file. Each random number should be 
# in the range of 1 through 500. The application should let the user specify how many random numbers 
# the file will hold.
#
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called generateFileOfRandomNumbers.  This function will be passed the name (including the path) of the file 
# that you'd like to create and the number of random numbers you'd like to put in this file.  The function will not return
# anything.
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

import random
def generateFileOfRandomNumbers(fileName, numberOfRandomNumbers):
        
        file = open(fileName, "w")
        for i in range(numberOfRandomNumbers):
                rand = random.randint(1,500)
                file.write(str(rand) + "\n")
                


        file.close()


	
#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

import random

def main():

        fileName = input("What is the name of the file of random numbers that you would like to generate? ")
        numberOfRandomNumbers = int(input("How many random numbers would you like to be written into " + fileName + "? "))
        generateFileOfRandomNumbers(fileName, numberOfRandomNumbers)

main()
