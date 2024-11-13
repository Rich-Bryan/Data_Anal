#
# AreaOfRectangles.py
#
# The area of a rectangle is the rectangle’s length times its width. Write a program that asks 
# for the length and width of two rectangles. The program should tell the user which rectangle 
# has the greater area, or if the areas are the same.
#


length1 = int(input("Enter length for rectangle 1: "))
width1 = int(input("Enter length for width 1 : "))

length2 = int(input("Enter length for rectangle 2: "))
width2 = int(input("Enter length for width 2 : "))

rec_1 = length1 * width1
rec_2 = length2 * width2

if rec_1 > rec_2:
    print("rectangle 1 is greater then rectangle 2")
elif rec_2 > rec_2:
    print("rectangle 2 is greater then rectangle 1")

else:
    print("they are the same")