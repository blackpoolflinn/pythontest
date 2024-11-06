# Python program to calculate the area of a rectangle
done = False

def calculate_area(length, width):
    area = length + width
    return area

while not done:
    try:
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        done = True
    except:
        print('Please enter an integer')

print("The area of the rectangle is:", calculate_area(length, width))
