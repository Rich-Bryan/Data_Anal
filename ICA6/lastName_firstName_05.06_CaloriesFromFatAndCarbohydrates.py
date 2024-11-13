#
# CaloriesFromFatAndCarbohydrates.py
#
# A nutritionist who works for a fitness club helps members by evaluating their diets. 
# As part of her evaluation, she asks members for the number of fat grams and carbohydrate 
# grams that they consumed in a day. Then, she calculates the number of calories that result 
# from the fat, using the following formula:
#
#    caloriesFromFat=fatGrams*9
#
# Next, she calculates the number of calories that result from the carbohydrates, using the following formula:
#
#    caloriesFromCarbs=carbGrams*4
#
# The nutritionist asks you to write a program that will make these calculations and displays the results.
#
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.

#
# Create a function called calculateCaloriesFromFat.  This function will be passed the number grams of fat and 
# will return the calories from this many grams of fat:
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def calculateCaloriesFromFat(fatGrams):
        caloriesFromFat = fatGrams*9
        return caloriesFromFat

	


#
# Create a function called calculateCaloriesFromCarbs here.  This function will be passed the number of grams of   
# carbs and will return the calories from this many grams of carbs:
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def calculateCaloriesFromCarbs(carbGrams):
        caloriesFromCarbs = carbGrams*4
        return caloriesFromCarbs
	
	

#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        fatGrams = float(input("How many grams of fat are consumed each day? "))
        carbGrams = float(input("How many grams of carbs are consumed each day? "))

        caloriesFromFat   = calculateCaloriesFromFat(fatGrams)
        caloriesFromCarbs = calculateCaloriesFromCarbs(carbGrams)

        print("The client is getting", caloriesFromFat, "calories when consuimg", fatGrams, "grams of fat")
        print("The client is getting", caloriesFromCarbs, "calories when consuimg", carbGrams, "grams of carbs")
        print("The total calories from fat and carbs is", caloriesFromFat + caloriesFromCarbs)

main()
