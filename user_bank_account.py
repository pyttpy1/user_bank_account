from copyreg import dispatch_table


class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        if amount > self.balance:
            self.balance -= 5
            print('not enough money charge a $5 fee')
        return self

    def display_account_info(self):
        print(f'Your balance is {self.balance} ')
        return self

    def yield_interest(self):
        self.balance = self.balance * (1 +self.int_rate)
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.balance += amount
        return self

user_money = User("Brandon","llll")
user_money.make_deposit(2000)
user_money.account.display_account_info()





