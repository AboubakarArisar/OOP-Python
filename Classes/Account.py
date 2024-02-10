#Account task in python

class Account:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Amount {amount} has been deposited to your account")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Amount {amount} has been withdrawn from your account")
        else:
            print("Insufficient balance")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"
    
    def __len__(self):
        return self.balance
    



acc = Account("John",1000)
print(acc)
print(len(acc))
acc.deposit(500)
print(acc)
acc.withdraw(200)
print(acc)
acc.withdraw(2000)
print(acc)

