#Lambda Functions (CO2)
#7 (a) Program to find square of a number using lambda Function.
m = int(input("Enter a number: "))
square = lambda m: m * m
print("Square of the first number is:", square(m))

#7 (b) Write lambda functions to find area of square, rectangle and triangle.
area_square = lambda s: s * s
area_rectangle = lambda l, b: l * b
area_triangle = lambda b, h: 0.5 * b * h

def calc_area(shape):
    shape = shape.lower()
    
    if shape == "square":
        s = float(input("Enter side: "))
        print(f"Area: {area_square(s)}")
        
    elif shape == "rectangle":
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        print(f"Area: {area_rectangle(l, b)}")
        
    elif shape == "triangle":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print(f"Area: {area_triangle(b, h)}")
        
    else:
        print("Invalid shape name entered.")

if __name__ == "__main__":
    shape_name = input("Enter shape name: ")
    calc_area(shape_name)
