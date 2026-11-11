class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    # Method to deposit money
    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount"
        self.balance += amount
        return amount

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        elif self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    # Method to check current balance
    def check_balance(self):
        print("Current Balance:", self.balance)

    # Method to display customer details
    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Balance:", self.balance)


# Create a bank account object
account1 = BankAccount("1234567890", 5000, "22-10-2026", "John Kamau")

# Test the methods
print("Deposited Amount:", account1.deposit(2000))
print("Withdrawn Amount:", account1.withdraw(1000))

account1.check_balance()
account1.customer_details()
