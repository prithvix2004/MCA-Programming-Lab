#2. List Operations
#2. (a) Create a list to store any five integers and display it.
num = [1, 2, 3, 4, 5]
print(num)

#2. (b) Create a list to store the days of a week and display the fifth day of the week.
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(week[4])

#2. (c) From a list of integers, create a list removing even numbers.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in range(1, 11):
    if(i % 2 != 0):
        b.append(i)

print(b)

#2. (d) Prompt the user for a list of integers. For all values greater than 100, store "over" instead.
list = []
new_list = []
limit = int(input("Enter a limit number : "))
for i in range(limit) :
    n = int(input("Enter a few numbers : "))
    list.append(i)
    if n > 100 :
        new_list.append('over')
    else :
        new_list.append(n)
print(new_list)

'''2. (e) Enter two lists of integers and check -
* Whether lists are of same length,
*  Whether list sums to same value,
* Whether any value occur in both.'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
b = [2, 4, 6, 8, 10, 12]

if (len(a) == len(b)) :
    print("The lists are of same length..")

else :
    print("The lists are of different length..")

if (sum(a) == sum(b)) :
    print("The sum are of same value..")

else :
    print("The sum are of different values..")
    
c = []

for num in a :
    if num in b :
        c.append(num)
        
print(f"The values that occur both are : {c}")
