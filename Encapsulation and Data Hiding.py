class BankAccount:
    def __init__(self, name, balance):
        self.name = name          
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance


# object creation
acc = BankAccount("Vedanti",6789)

# accessing 
print("Account Holder:", acc.name)

# accessing 
print("Balance:", acc.get_balance())

# deposit  amount
acc.deposit(2344)
print("Updated Balance:", acc.get_balance())
