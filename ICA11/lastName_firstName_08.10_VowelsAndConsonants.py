#
# VowelsAndConsonants.py
#
# Write a program with a function that accepts a string as an argument and returns the number of 
# vowels that the string contains. The program should have another function that accepts a 
# string as an argument and returns the number of consonants that the string contains. The 
# application should let the user enter a string, and should display the number of vowels and 
# the number of consonants it contains.
#
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.
#
#
# Create a function called findNumberOfVowels.  This function is passed a string and returns the number of vowles
# in the string: 
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def findNumberOfVowels(stringToAnalyze):
    vowels = "aeiouAEIOU"
    count = 0
    for char in stringToAnalyze:
        if char.isalpha() and char in vowels:
            count += 1
    return count

	

#
# Create a function called findNumberOfConsonants.  This function is passed a string and returns the number of consonants
# in the string: 
#
#################################################################################################################
#                                                                                                               #
# Please note that the functaion declaration has been provided for you.  Do not change the function declaration #
# in any way.  Write the code that makes up the function without altering the function declaration.  For graded #
# assignments and for programs that are part of exams, if you alter the function declaration you will not       #
# receive credit for your work.  This will be disussed in class.                                                #
#                                                                                                               #  
#################################################################################################################

def findNumberOfConsonants(stringToAnalyze):
    vowels = "aeiouAEIOU"
    count = 0
    for char in stringToAnalyze:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

	

#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        stringToAnalyze = input("Enter a string and press 'Enter' to find the number of vowels and consonants in the string: ")
        numberOfVowels = findNumberOfVowels(stringToAnalyze)
        numberOfConsonants = findNumberOfConsonants(stringToAnalyze)
        
        print("Number of vowels:    ", numberOfVowels)
        print("Number of consonants:", numberOfConsonants)

main()
