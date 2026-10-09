#3. Function Programs
#3. (a) Function program to print "Hello World".
def func():
    print("Hello World..")
func()

#3. (b) Function program to display "Hello ----" by filling dash with your name stored in variable 'Name'.
name = input("Enter your name : ")

def func():
    print(f"Hello, {name}..")

func()

#3. (c) Find the sum and product of three numbers using a function.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

Sum = a + b + c
Product = a * b * c

def sum():
    print(f"Sum is {Sum}")
    
def product():
    print(f"Product is {Product}")

sum()
product()

#3. (d) Display future leap year from current year to a final year entered by user using a function.
cyear = int(input("Enter current year : "))
fyear = int(input("Enter final year : "))
year = []

def lyear():
    for i in range(cyear, fyear + 1):
        if(i % 4 == 0 and i % 100 != 0) or (i % 400 == 0) :
            year.append(i)
    print(year)

lyear()
