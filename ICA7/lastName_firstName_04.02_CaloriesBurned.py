#
# CaloriesBurned.py
#
# Running on a particular treadmill you burn 4.2 calories per minute. Write a program that 
# uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
#
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called caloriesBurned.  Nothing will be passed to this function and nothing will be returned
# by this function.  When the function is invoked, it will utilize a loop to display the required information:  
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def caloriesBurned():
        calorie_burn_per_minute = 4.2
        for i in range(10,31,5):
                print(calorie_burn_per_minute*i)
                
                

	
	
#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        caloriesBurned()

main()
