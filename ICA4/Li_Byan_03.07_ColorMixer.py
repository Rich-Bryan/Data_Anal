#
# ColorMixer.py
#
# The colors red, blue, and yellow are known as the primary colors because they cannot be made by 
# mixing other colors. When you mix two primary colors, you get a secondary color, as shown here:
#
#    When you mix red and blue, you get purple.
#    When you mix red and yellow, you get orange.
#    When you mix blue and yellow, you get green.
#
#    Note that the order doesn't matter.  That is, blue and red also give you purple.
#    Also note that if you mix two of the same color, you just get more of that same color.
#
# Design a program that prompts the user to enter the names of two primary colors to mix. If the 
# user enters anything other than “red,” “blue,” or “yellow,” the program should display an error message. 
# Otherwise, the program should display the name of the secondary color that results.
#



# Define the set of primary colors
primary_colors = ["red", "blue", "yellow"]


color1 = input("Enter the first primary color (red, blue, yellow): ")
color2 = input("Enter the second primary color (red, blue, yellow): ")


if color1 not in primary_colors or color2 not in primary_colors:
    print("Please enter: 'red', 'blue', or 'yellow'.")
else:
    if color1 == color2:
        print("The result is ", color1)
    elif (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
        print("The result is purple.")
    elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
        print("The result is orange.")
    elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
        print("The result is green.")
