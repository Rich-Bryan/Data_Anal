#
# FileDisplay.py
#
# Your instructor has provinded you access to a file named numbers.txt. 
#
# Write a program that displays all of the numbers in the file.
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called displayFileContents.  This function will not be passed anything and will not return anything.
# The function will open numbers.txt, read and display the contents of numbers.txt and close numbers.txt: 
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def displayFileContents():

#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
        # this will automatically close the file
        with open("ICA9/numbers.txt", "r") as output:
                print(output.read())



def main():
        
        displayFileContents()

main()
