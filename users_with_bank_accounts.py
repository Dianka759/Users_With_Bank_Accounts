class BankAccount:
    # accounts = []

    def __init__(self, interest, balance=0):
        self.interest = interest
        self.balance = balance
        # BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        return self.balance
        

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest
        else:
            print("No interest acquired because balance is negative")
        return self

    # @classmethod
    # def print_all_accounts(cls):
    #     print("All instances of a Bank Account's info:")
    #     for account in cls.accounts:
    #         account.display_account_info()


class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.02, 0), #creating a checkings account with default interest and balance
            "savings" : BankAccount(.10,1000) #creating a savings account with default interest and balance
        }

    def display_balance(self): # prints both statements, stating the balance of both the cheking and savings accounts
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")  #display_account_info returns the current balance of the bank account
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    # def transfer_money(self, other_user, amount):
    #     self.account -= amount  
    #     other_user.account += amount
    #     return self


diana = User("Diana")
kiwi = User("Kiwi")


diana.account['checking'].deposit(100).withdraw(50)
diana.account['savings'].deposit(777)
diana.display_balance()
print() #for visual purposes, to separate the two users 
kiwi.account['checking'].deposit(50).deposit(100).withdraw(1000)
kiwi.account['savings'].deposit(900).withdraw(5)
kiwi.display_balance()


