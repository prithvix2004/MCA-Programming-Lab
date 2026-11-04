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
