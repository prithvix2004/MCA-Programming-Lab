#10. File Operations (CO5)
# 10 (a) Write a Python program to read a file line by line and store it into a list.
# Opening the file (after creating a text file)
f = open("sample.txt", "r")

# Reading lines and storing them in a list
lines = []

for line in f:
    lines.append(line.strip())

# Displaying the list
print(lines)

# Closing the file
f.close()

# 10 (b) Python program to copy odd lines of one file to other.
# Opening source file in read mode
f1 = open("source.txt", "r")

# Opening destination file in write mode
f2 = open("destination.txt", "w")

# Reading lines one by one
lines = f1.readlines()

for i in range(len(lines)):
    if i % 2 == 0:
        f2.write(lines[i])

# Closing files
f1.close()
f2.close()

print("Odd lines copied successfully!")

#10 (c) Write a Python program to read each row from a given csv file and print a list of strings.
import csv

# Opening the CSV file
f = open("sample.csv", "r")

# Reading each row
reader = csv.reader(f)

for row in reader:
    print(row)

# Closing the file
f.close()

# 10 (d) Write a Python program to read specific columns of a given CSV file and print the content of the columns.
import csv

# Opening the CSV file
f = open("sample.csv", "r")

reader = csv.reader(f)

# Reading each row
for row in reader:
    print(row[0], row[2])

# Closing the file
f.close()
