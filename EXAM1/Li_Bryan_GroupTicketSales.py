####################################################################################################
#                                                                                                  #
# After downloading this file, rename it by replacing `lastName` with your last name and           #
# `firstName` with your first name. Do **not** modify any other parts of the file name.            #
# The other parts are necessary for accurate grading. Changing them may result in your work        #
# not being graded, and you may not receive credit. If you have any questions, contact your        #
# instructor or ITA.                                                                               #
#                                                                                                  #
# The main program has been provided for you, performing basic input and output.                   #
# Your task is to implement the missing functions, which have been defined but left blank.         #
# Do **not** modify the function declarations. Changing these will prevent proper grading,         #
# and you may not receive credit for your work. If anything is unclear, speak with your            #
# instructor or ITA.                                                                               #
#                                                                                                  #
####################################################################################################
#                                                                                                  #
# Program: Group Ticket Sales                                                                      #
#                                                                                                  #
# The Philadelphia Metropolitan Opera House has recently re-opened on North Broad Street.          #
# They are offering a concert series focused on local artists, including a "season ticket"         #
# package that provides admission to all concerts in the series.                                   #
#                                                                                                  #
# The Group Ticket Sales group is selling blocks of season tickets to small groups,                #
# which include an entire box (seating 12 to 18 people) at a fixed price. There is an additional    #
# fee for each person beyond 18 people.                                                            #
#                                                                                                  #
# Individual season tickets cost $500 each. For groups of 12 to 18 people, a box can be            #
# purchased at a fixed price of $6,000, regardless of the exact number (e.g., 12, 13, ... 18).      #
# However, if your group has more than 18 people, each extra person will be charged an additional  #
# $200 per ticket.                                                                                 #
#                                                                                                  #
# Write a function that takes the number of people in the group and returns the total              #
# ticket cost for the group.                                                                       #
#                                                                                                  #
####################################################################################################

def calculateGroupTicketPrice(numberOfPeople):
    seasonTicket = 500
    boxTicket  = 6000 # fix price for more >= 12 and <= 18

    # for less than 12 
    if numberOfPeople < 12:
        return numberOfPeople*500
    # for greater than 12 and less than 18
    elif numberOfPeople >= 12 and numberOfPeople <= 18:
        return boxTicket
    elif numberOfPeople > 18:
        # charge extra fee (200) if number of people over 18, only people over 19 and the extra 1 will be 1 extra so that person will get charge extra 200
        return boxTicket + ((numberOfPeople-18)*200)

    ################################################################################################
    # Implement your solution here. Do not modify the function declaration above.                  #
    ################################################################################################

	
####################################################################################################
# This is the main part of the program. Do not modify any code below this comment. Simply update   #
# the code in the functions above.                                                                 #
####################################################################################################
	
people = int(input('How many people are in your group? '))

print('The cost of season tickets for ' + str(people) + ' is $' + str(calculateGroupTicketPrice(people)))