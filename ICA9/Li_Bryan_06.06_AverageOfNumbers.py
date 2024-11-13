#
# AverageOfNumbers.py
#
# Your instructor has provided you access to a file that contains a series of integers named numbers.txt. 
#
# Write a program that calculates the average of all the numbers stored in the file.
#
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called returnAverage.  This function will be passed the name (including the path) of the file 
# that you'd like to process.  The function will return the average of the records in the file.
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def returnAverage(fileName):
        # file = open("ICA9/numbers.txt", "r")
        file = open(fileName, "r")
        total = 0
        n = 0
        for num in file:
                line = num.strip()
                total+=int(line)
                n +=1
        return total/n

        file.close()
	
#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        fileName = input("What is the file name that you'd like to display average of the records? ")
        averageOfRecords = returnAverage(fileName)
        print("The average of the records in", fileName, "is", averageOfRecords)

main()
