# 11. Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content.
import csv

# Creating a dictionary
data = [
    {"Name": "Alexandra", "Age": 22, "Course": "MCA"},
    {"Name": "Blanc", "Age": 21, "Course": "BCA"},
    {"Name": "Cassandra", "Age": 23, "Course": "BSc"}
]

# Writing dictionary to CSV file
f = open("sample.csv", "w", newline="")

fields = ["Name", "Age", "Course"]

writer = csv.DictWriter(f, fieldnames=fields)
writer.writeheader()
writer.writerows(data)

f.close()

# Reading CSV file
f = open("sample.csv", "r")

reader = csv.reader(f)

print("Contents of CSV file:")

for row in reader:
    print(row)

f.close()
