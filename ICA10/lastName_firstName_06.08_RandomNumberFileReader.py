#
#
# RandomNumberFileReader.py
#
# This exercise assumes you have completed Programming Exercise 7, Random Number File Writer. Write another 
# program that reads the random numbers from the file, displays the numbers, then displays the following data:
#
#    The number of random numbers read from the file
#    The total of the numbers
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called returnAverage.  This function will be passed the name (including the path) of the file 
# that you'd like to process.  The function will loop through the contents of the file and display the number of
# records in the file.  The function will then return the total of all of the records in the file.
#
# Suggestion: pass the steps.txt file to your program.  It is a list of integers.
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################
                
                

def processFile(fileName):
         with open(fileName, 'r') as file:
                records = file.readlines()
                total = 0
                record_count = len(records)
                for record in records:
                        total += int(record)
                        # print(record.strip())
                print("avg", total/record_count)
                print(record_count)
                return record_count


	
	
#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        fileName = input("What is the file name that you'd like to process? ")
        recordSum = processFile(fileName)
        print(fileName, "The total is", recordSum)

main()
