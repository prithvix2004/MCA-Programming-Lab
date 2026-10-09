#1. Integer Operations
#1. (a) Accept the radius from a user to find the area of the circle.
radius = int(input("Enter a radius : "))
area = 3.14*radius*radius
print("Area is : ", area)

#1. (b) Find the biggest of three numbers entered.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if(a>b and a>c):
    print(f"{a} is the largest..")
elif(a<b and b>c):
    print(f"{b} is the largest..")
else:
    print(f"{c} is the largest..")

#1. (c) Accept an integer n and compute n + nn + nnn.
num=int(input("Enter a number : "))

sum=num+(num*10+num)+(num*100+num*10+num)
print(f"Sum is : {sum}")

#1. (d) Find the greatest common divisor (GCD) of two numbers.
import math
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
gcd = math.gcd(a,b)
print(f"GCD : {gcd}")
