#String and Dictionary Operations
#5 (a) Store a list of first names. Count the occurances of 'a' within the list.
fname = ["Akash", "Anushya", "Gowri", "Kiran", "Prithvi"]
s = sum(i.lower().count('a') for i in fname)
print(s)

#5 (b) Get a string from an input string where all occurences of first character replaced with '$', except the first character.
string = input("Enter a string : ")
if string :
    fc = string[0]
    r = fc + string[1 : ].replace(fc, '$')
    print(r)

#5 (c) Create a string from given string where first and last characters exchanged.
string = input("Enter a string : ")
if len(string) > 1 :
    r = string[-1] + string[1 : -1] + string[0]
    print(r)

#5 (d) Accept a file name from user and print extension of that.
filename = input("Enter a filename : ")
if "." in filename :
    extension = filename.split(".")[-1]
    print(extension)

#5 (e) Count the occurences of each word in a line of text.
text = "mango pineapple papaya mango pineapple papaya mango pineapple papaya mango pineapple papaya"
words = text.split()

wcount = {}
for word in words:
    wcount[word] = wcount.get(word, 0) + 1

print(wcount)

#5 (f) Create a list of colors from comma - separated color names entered by user. Display first and last colors.
color_list = input("Enter a list of colors separated by comma : ")
color = color_list.split(",")
print((color[0], color[-1]))

#5 (g) Print out all colors from color - list1 not contained in color - list2.
color_list1 = ["Black", "Red", "Green", "Navy Blue"]
color_list2 = ["White", "Maroon", "Green", "Navy Blue"]
output = [color for color in color_list1 if color not in color_list2]
print(output)

#5 (h) Create a single string separated with space from two strings by swapping the character at position 1.
string1 = input("Enter a string : ")
string2 = input("Enter a string : ")

new_string = string2[0] + string1[1] + string1[2:]
new_string2 = string1[0] + string2[1] + string2[2:]

result = new_string + " " + new_string2

print(result)

#5 (i) To store and display the contents of a dictionary.
x = {
    "name" : "Prithvi",
    "age" : 22,
    "occupation" : "College Student"
}
print(x)

#5 (j) Sort dictionary in ascending and descending order.
dictionary={
    "Apple" : 1,
    "Pineapple" : 2,
    "Banana" : 3,
    "Cherry" : 4
}
dictionary_ascendingorder = dict(sorted(dictionary.items()))
dictionary_descendingorder = dict(sorted(dictionary.items(),reverse = True))
print("Ascending Order", dictionary_ascendingorder)
print("Descending Order", dictionary_descendingorder)

#5 (k) Merge two dictionaries.
dict1 = {"A" : 10, "B" : 20}
dict2 = {"C" : 30, "D" : 40}
merge = dict1|dict2
print(merge)
