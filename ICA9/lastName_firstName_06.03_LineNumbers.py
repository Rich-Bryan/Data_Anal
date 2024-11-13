#
# LineNumbers.py
#
# Write a program that asks the user for the name of a file. The program should display the 
# contents of the file with each line preceded with a line number followed by a colon. The 
# line numbering should start at 1.
#
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called displayFileWithLinenumbers.  This function will be passed the name (including the path) of the file 
# that you'd like to display the first five lines of.  The function will not return anything, it will simply display
# the contents of the file with each line prefaced with a line number:
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def displayFileWithLinenumbers(fileName):
        with open(fileName, "r") as file: 

                lineCounter = 0
                while lineCounter < 5:
                        line = file.readline()  
                        print("line: ", lineCounter+1, line.rstrip())
                        lineCounter+=1


                        
                   

	
#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():
        
        fileName = input("What is the file name that you'd like to display with record numbers? ")
        displayFileWithLinenumbers(fileName)

main()
        
