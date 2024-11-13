#
# AutomobileCosts.py
#
# Write a program that asks the user to enter the monthly costs for the following expenses 
# incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, 
# and maintenance. The program should display the total monthly cost of these expenses.
#
#
# The main program has been created for you.  The main program will get some input from the user, invoke one or
# more functions to do the actual work and display some output.  Your job will be to create/update the function 
# that does the actual work and returns the results to the main program.

#
# Create a function called totalUpMonthlyAutomobileCosts here.  This function will not be passed anything but will 
# prompt the user for the monthly amount of the loan payment, insurance, gas, oil, tiers, and maintenance costs.
# the function will add up and return the sum of these values:
#

def totalUpMonthlyAutomobileCosts():
        loan_payment = float(input("Enter the monthly loan payment: "))
        insurance = float(input("Enter the monthly insurance cost: "))
        gas = float(input("Enter the monthly gas cost: "))
        oil = float(input("Enter the monthly oil change cost: "))
        tires = float(input("Enter the monthly tires cost: "))
        maintenance = float(input("Enter the monthly maintenance cost: "))

        total_cost = loan_payment + insurance + gas + oil + tires + maintenance

        return total_cost


#
# The main program starts here through the end of the file.  You should not be making any changes to the 
# main program.  You should only be creating/updating the functions defined above.
#

def main():

        monthlyAutomobileCosts = totalUpMonthlyAutomobileCosts()
        print("The total monthly automobile costs are", monthlyAutomobileCosts)

main()
