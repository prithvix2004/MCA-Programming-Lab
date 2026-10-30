#Lambda Functions (CO2)
#7 (a) Program to find square of a number using lambda Function.
m = int(input("Enter a number: "))
square = lambda m: m * m
print("Square of the first number is:", square(m))

#7 (b) Write lambda functions to find area of square, rectangle and triangle.
def calc_area(shape):
    shape = shape.lower()

    if shape == "square":
        s = float(input("Enter side: "))
        print(f"Area: {s * s}")

    elif shape == "rectangle":
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        print(f"Area: {l * b}")

    elif shape == "triangle":
        h = float(input("Enter height: "))
        b = float(input("Enter base: "))
        print(f"Area: {0.5 * b * h}")
        
if __name__ == "__main__":
    shape_name = input("Enter shape name: ")
    calc_area(shape_name)
