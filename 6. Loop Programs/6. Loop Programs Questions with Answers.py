#Loop Programs (CO2)
#6 (a) Program to find the factorial of a number.
n = int(input("Enter a number : "))
if n < 0:
    print("Factorial is not defined for negative numbers.. Try again..")
else:
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f)

#6 (b) Generate Fibonacci series of N terms.
n = int(input("Enter number of terms : "))
a, b = 0, 1

for i in range(n) :
    print(a, end = " ")
    a, b = b, a + b

#6 (c) Find the sum of all items in a list.
a = [10, 20, 30, 40, 50]
res = 0 # Initialize sum variable

for i in a:
    res += i 
print(res)

#6 (d) Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square.
def four_digit_even_digit_squares(start, end):
    result = []
    for n in range(int(start ** 0.5), int(end ** 0.5) + 1):
        sq = n * n
        if start <= sq <= end:
            digits = str(sq)
            if all(int(d) % 2 == 0 for d in digits):
                result.append(sq)
    return result

print(four_digit_even_digit_squares(1000, 9999))

'''6 (e) Display the given pyramid with step number accepted from user.
Like :
1
2 4
3 6 9
4 8 12 16'''
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()

#6 (f) Count the number of characters (character frequency) in a string.
input_string = "Hello, World!"
char_frequency = {}
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(char_frequency)

#6 (g) Add 'ing' at the end of a given string. If it already ends with 'ing', then add 'ly'.
def add_suffix(string):
   if len(string) < 3:
       return string
   elif string.endswith('ing'):
       return string + 'ly'
   else:
       return string + 'ing'

print(add_suffix('abc'))
print(add_suffix('string'))
print(add_suffix('ab'))

#6 (h) Accept a list of words and return length of longest word.
a = ["Welcome", "to", "Python", "programming"]

# Use max() with key=len to find the word with the maximum length
res = len(max(a, key=len))
print(res)

'''6 (i) Construct following pattern using nested loop.
*
* *
* * *
* * * *
* * *
* *
*'''
n=int(input("enter the number of row: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j, end=" ")
    print()

#6 (j) Generate all factors of a number.
n = int(input("Enter a number : "))
factors = [i for i in range(1, n + 1) if n % i == 0]
print(factors)
