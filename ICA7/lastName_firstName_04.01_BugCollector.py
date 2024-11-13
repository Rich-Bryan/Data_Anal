#
# BugCollector.py
#
# A bug collector collects bugs every day for five days. Write a program that keeps a running 
# total of the number of bugs collected during the five days. The loop should ask for the number 
# of bugs collected for each day, and when the loop is finished, the program should display the 
# total number of bugs collected.
#
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called bugsCollected.  Nothing will be passed to this function.  It will us a loop and keep 
# a running toal of the number of bugs collected each day over a five day period.  The function will return the 
# total number of bugs collected over this time.  
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def bugsCollected():
        bug_collected_each_day = int(input("Enter number of bugs collected each day: "))
        total = 0
        for i in range(5):
                total += bug_collected_each_day
        return total
	
#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        print("Over a five day period,", bugsCollected(), "bugs were collected.")

main()
