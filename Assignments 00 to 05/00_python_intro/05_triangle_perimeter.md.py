# Get the 3 side lengths of the triangle
side1 = float(input("What is the length of side 1? "))
side2 = float(input("What is the length of side 2? "))
side3 = float(input("What is the length of side 3? "))

#Print out the perimeter (sum of the sides) of the triangle, make sure to cast it to a str when concatenating
perimeter = side1 + side2 + side3

# Perimeter print
print(f"The perimeter of the triangle is {perimeter}")