# Python program to calculate the area of a rectangle

def calculate_area(length, width):
    area = length + width
    return area

length = input("Enter the length of the rectangle: ")
width = input("Enter the width of the rectangle: ")

length = int(length)
width = int(width)

print("The area of the rectangle is:", calculate_area(length, width))
