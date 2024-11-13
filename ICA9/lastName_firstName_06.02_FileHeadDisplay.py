#
# FileHeadDisplay.py
#
# Write a program that asks the user for the name of a file. The program should display only the 
# first five lines of the file’s contents. If the file contains less than five lines, it should 
# display the file’s entire contents.
#
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called displayFileHead.  This function will be passed the name (including the path) of the file 
# that you'd like to display the first five lines of.  The function will not return anything, it will simply display
# the first five lines of the file (fewere lines if it has fewer than five lines) and return to the main program.
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def displayFileHead(fileName):
        with open(fileName, "r") as output: 
                for i in range(5):
                        print(output.readline(), end="")

	
#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():
        
        fileName = input("What is the file name that you'd like to display the first five lines from? ")
        displayFileHead(fileName)

main()
