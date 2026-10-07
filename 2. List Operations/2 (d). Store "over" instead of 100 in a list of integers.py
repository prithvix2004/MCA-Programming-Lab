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
