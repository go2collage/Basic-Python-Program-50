# Python Program

# Methods with same name but different number of parameters.

# create class
class Cal_Area():

    # Define Methods
    def area(self, length, breadth):
        print(length * breadth)

    def area(self, side):
        print(side * side)

# Creating class instance
a = Cal_Area()

# Call Methods
# print("Area of Square is: ", a.area(1))

print("Area of Rectangle is: ", a.area(3, 50))

a.area(1)

