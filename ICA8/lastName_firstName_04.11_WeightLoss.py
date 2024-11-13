#
# WeightLoss.py
#
# If a moderately active person cuts their calorie intake by 500 calories a day, they can typically 
# lose about 4 pounds a month. Write a program that lets the user enter their starting weight, then 
# creates and displays a table showing what their expected weight will be at the end of each month 
# for the next 6 months if they stay on this diet.
#
# Your program must use a loop to display this information.  For example, your output should look something like: 
#
#    What is your starting weight? 130
#    Starting at 130.0 pounds, after 1 month(s) your weight should be 126.0 pounds.
#    Starting at 130.0 pounds, after 2 month(s) your weight should be 122.0 pounds.
#    Starting at 130.0 pounds, after 3 month(s) your weight should be 118.0 pounds.
#    Starting at 130.0 pounds, after 4 month(s) your weight should be 114.0 pounds.
#    Starting at 130.0 pounds, after 5 month(s) your weight should be 110.0 pounds.
#    Starting at 130.0 pounds, after 6 month(s) your weight should be 106.0 pounds.
#    At the end of the 6 month period, your projected weight will be 106.0
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called displaytWeightLoss.  This function will be passed the starting weight.  The function 
# will return the estimated weight at the end of the 6 month period.  The function will also show the estimated 
# weight at the end of each month during the 6 month period:  
#
# The value returned needs to be a number, either a floating point number or an integer, not a string that may 
# include characters like the dollar character ("$") or the comma (",") used as a thousands separator.
#
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def displayWeightLoss(startingWeight):
        losing_weight = startingWeight
        for i in range(6):
                losing_weight -= 4 
                print(f"Starting at {startingWeight} pounds, after {i+1} month(s) your weight should be {losing_weight} pounds.")
        return losing_weight



	

#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        startingWeight = float(input("What is your starting weight? "))
        projectedWeight = displayWeightLoss(startingWeight)
        print("At the end of the 6 month period, your projected weight will be", projectedWeight)

main()
