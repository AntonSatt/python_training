class BankAccount:
    """A simple bank account class"""
    
    def __init__(self):
        # TODO: Fix the initialization
        self.balance = 100
    
    def deposit(self, amount):
        # TODO: Fix the deposit logic
        pass
    
    def withdraw(self, amount):
        # TODO: Fix the withdrawal logic (prevent overdraft)
        self.balance = self.balance - amount
    
    def get_balance(self):
        # TODO: Fix to return the actual balance
        return 0


if __name__ == "__main__":
    account = BankAccount()
    account.deposit(150)
    print(f"Balance: {account.get_balance()}")
    account.withdraw(50)
    print(f"After withdrawal: {account.get_balance()}")
