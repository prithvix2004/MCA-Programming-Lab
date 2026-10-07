#2. (c) From a list of integers, create a list removing even numbers.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in range(1, 11):
    if(i % 2 != 0):
        b.append(i)

print(b)
