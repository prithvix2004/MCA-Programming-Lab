#9. Class operations 
#9 (a) Create Rectangle class with attributes length and breadth and methods to find area and perimeter. Compare two Rectangle objects by their area.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def __lt__(self, other):
        return self.area() < other.area()

#Example
rect1 = Rectangle(10, 5)
rect2 = Rectangle(8, 7)

print("Rectangle 1 is smaller:", rect1 < rect2)

#9 (b) Create a Bank account with members account number, name, type of account and balance.
class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = float(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        return self.balance

    def __str__(self):
        return f"Acc No: {self.account_number} | Holder: {self.name} | Type: {self.account_type} | Balance: ${self.balance:.2f}"


# Example:
if __name__ == "__main__":
    acc = BankAccount("10012345", "Alice Johnson", "Savings", 500.00)
    acc.deposit(150.50)
    acc.withdraw(50.00)
    print(acc)

#9 (c) Write constructor and methods to deposit at the bank and withdraw an amount from the bank.
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Insufficient Balance!")


# Creating an object
b = Bank("User", 5000)

# Calling methods
b.deposit(2000)
b.withdraw(1000)

#9 (d) Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to compare the area of 2 rectangles.
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()


# Creating objects
r1 = Rectangle(10, 5)
r2 = Rectangle(8, 4)

# Comparing areas
if r1 < r2:
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 1 does not have smaller area")

#9 (e) Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to find sum of 2 time.
class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        total = (self.__hour * 3600 + self.__minute * 60 + self.__second) + \
                (other.__hour * 3600 + other.__minute * 60 + other.__second)

        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60

        return Time(h, m, s)

    def display(self):
        print(self.__hour, ":", self.__minute, ":", self.__second)


# Creating objects
t1 = Time(2, 30, 40)
t2 = Time(1, 45, 30)

# Adding two times
t3 = t1 + t2

print("Sum of two times:")
t3.display()

#9 (f) Create a class Publisher (name). Derive class Book from Publisher with attributes title and author. Derive class Python from Book with attributes price and number of pages. Write a  program that displays information about a Python book. Use base class constructor invocation and method overriding.
class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher Name:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Book Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages

    def display(self):
        super().display()
        print("Price:", self.price)
        print("Number of Pages:", self.pages)


# Creating an object
p = Python("ABC Publications", "Python Programming",
           "John Smith", 450, 300)

# Displaying book information
p.display()
