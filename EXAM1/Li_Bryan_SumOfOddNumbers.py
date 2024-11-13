####################################################################################################
# SumOfOddNumbers.py                                                                               #
#                                                                                                  #
# Instructions:                                                                                    #
#                                                                                                  #
# The main program has been provided for you. Your task is to create and complete the function     #
# `addUpOddNumbers`, which performs the required computation and returns the result to the main    #
# program. The main program will then display the returned value.                                  #
#                                                                                                  #
# Task:                                                                                            #
# Create a function named `addUpOddNumbers` that:                                                  #
# - Does not take any arguments.                                                                   #
# - Uses a for loop with the `range()` function to sum all the odd numbers from 1 up to 99.        #
# - Returns the total sum to the main program.                                                     #
#                                                                                                  #
####################################################################################################
#                                                                                                  #
# Important Note:                                                                                  #
# Do not modify the function declaration.                                                          #
# The function declaration has been provided for you and is required for correct grading.          #
# If you change the function declaration, you may not receive credit for your work.                #
#                                                                                                  #
####################################################################################################

def addUpOddNumbers():
    sumOdd = 0
    for i in range(100):
        if (i % 2) != 0:
            print(i)
            sumOdd += i
    return sumOdd
        

    ################################################################################################
    # Implement the solution here.                                                                 #
    ################################################################################################


####################################################################################################
# The main program starts here and should not be modified. Make updates only to the function above.#
####################################################################################################

def main():

        print("The sum of odd numbers between 1 and 99 is", addUpOddNumbers())

main()
