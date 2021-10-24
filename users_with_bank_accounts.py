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
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

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
        self.account = BankAccount(interest=.02, balance=0)

    def deposit(self, amount):
        self.account.deposit(amount)
        return self

    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")
        return self

    # def transfer_money(self, other_user, amount):
    #     self.account -= amount  
    #     other_user.account += amount
    #     return self


diana = User("Diana")
kiwi = User("Kiwi")


diana.deposit(1000).withdraw(100).display_balance()
print()
kiwi.deposit(50).deposit(100).withdraw(200).display_balance()

