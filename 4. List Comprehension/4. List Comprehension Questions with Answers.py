#4. List Comprehension
#4. (a) Generate positive list of numbers from a given list of integers.
n = [1, 2, 3, 4, 5, 6, -2, -4]
list = [i for i in n if i>0]
print(list)

#4. (b) Square of N numbers.
n = [2, 4, 6, 8, 10]
sq = [x**2 for x in n]
print(sq)

#4. (c) Form a list of vowels selected from a given word.
word = "Hello"
a = [char for i in word for char in i.lower() if char in "aeiou"]
print(a)

#4. (d) List ordinal value of each element of a word. (Hint : use ord() to get ordinal values.)
word = "Hello"
a = [ord(char) for char in word]
print(a)
