####################################################################################################
#                                                                                                  #
# After downloading this file, please change the file name of the file replacing lastName with     #
# your last name and firstName with your first name.  Do not change other parts of the file name.  #
# The other parts of the file name are required for your work to be graded properly.  If you       # 
# change other parts of the file name, your work will not be graded and you will not receive       #
# credit for your work.  Speak with your instructor if this is not clear.                          #  
#                                                                                                  #
# The main program has been provided for you.  The main program simply performs simple input and   #
# output.  The real work, and your challenge, is to fill in the functions which have been defined  #
# but have been left blank.    Speak with your instructor or your TA if this is not clear.         #
#                                                                                                  #
# Do not change the function declarations.  They have been provided and are required for your work # 
# to be graded properly.  If you change parts of the function declarations, your work will not be  #
# graded and you will not receive credit for your work.  Speak with your instructor or your TA if # 
# this is not clear.                                                                               #
#                                                                                                  #
####################################################################################################
#                                                                                                  #
# Program: Philly Restaurants                                                                      #
#                                                                                                  #
# Philly is a town that has lots of exciting restaurants.  This program includes a short list of   #
# restaurants located in Philly.  When someone runs this program, they will be prompted to enter   #
# the name of a restaurant.  The program will then display a message indicating if the restaurant  #
# is in the short list of Philly restaurants or not.                                               #
#                                                                                                  #
# For example, if a known restaurant like Mixto Restaurante is entered, the program should         #
# display:                                                                                         #
#                                                                                                  #
#      What is the name of the restaurant? Mixto Restaurante                                      #
#      Mixto Restaurante is on the list of Philly restaurants.                                     #
#                                                                                                  #
# However, if an unknown restaurant like Parks Diner is entered, the program should display:       #
#                                                                                                  #
#      What is the name of the restaurant? Parks Diner                                             #
#      Parks Diner is not on the list of Philly restaurants                                        #
#                                                                                                  #
# The main program has been written for you.  Do not update the main program.  The main program    #
# creates and populates the list of Philly restaurants and then prompts the user for the name of   #
# a restaurant that may or may not be on this list.  The main program will call isAPhillyRestaurant#
# function to determine if the restaurant is on the list and then display the appropriate message  #
#                                                                                                  #
# Your job is to write the code for isAPhillyRestaurant. isAPhillyRestaurant is passed two things. #
# The first is the list of Philly restaurants.  The second is the name of the restaurant to check  #
# in the list of Philly restaurants.  isAPhillyRestaurant is a Boolean function that returns either#
# the value True or the value False.  The function will search the list for the restaurant.        #
# If the restaurant is found, the function will return the value True.  If the restaurant is not   #
# found, the function will return the value False.                                                 #
#                                                                                                  #
####################################################################################################

def isAPhillyRestaurant(listOfPhillyRestaurants, thisRestaurant):
    ################################################################################################
    # You must add your code to this part of this function.  Do not change the function            #
    # declaration above.                                                                           #
    ################################################################################################
    if thisRestaurant in listOfPhillyRestaurants:
        return thisRestaurant + " is on the list of Philly restaurants."
    else:
        return thisRestaurant + " is not on the list of Philly restaurants"



####################################################################################################
# This is the main part of the program.  Do not change any code below this comment.  Simply update #
# code in the functions above.                                                                     #
####################################################################################################

def main():
    
    listOfPhillyRestaurants = [
        "Mixto Restaurante",
        "JJ Thai Cuisine",
        "Terakawa Ramen",
        "Hershel's East Side Deli",
        "Jose Pistola's",
        "Giuseppe & Sons",
        "Ninja Sushi & Hibachi Japanese Restaurant",
        "Gilda",
        "Chili's Grill & Bar",
        "Veda - Modern Indian Bistro",
        "Masala Kitchen: Kati Rolls and Platters",
        "Saad's Halal Restaurant",
        "McGillin's Olde Ale House",
        "Huda",
        "Ocean City Restaurant",
        "Kim's Restaurant",
        "Sampan",
        "Bubblefish",
        "DBG Philly",
        "Angelo's Pizzeria",
        "Bonchon Philadelphia",
        "DanDan Rittenhouse",
        "Green Eggs Cafe",
        "Hardena",
        "R&D Cocktail Bar",
        "K'Far Cafe Philadelphia",
        "Big Ass Slices Bar & Grill"
    ]

    thisRestaurant = input('What is the name of the restaurant? ')

    if isAPhillyRestaurant(listOfPhillyRestaurants, thisRestaurant):
        print(thisRestaurant, "is on the list of Philly restaurants.")
    else:
        print(thisRestaurant, "is not on the list of Philly restaurants")
    

main()
