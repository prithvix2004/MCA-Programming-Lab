#1. (c) Accept an integer n and compute n + nn + nnn.
num=int(input("Enter a number : "))

sum=num+(num*10+num)+(num*100+num*10+num)
print(f"Sum is : {sum}")
