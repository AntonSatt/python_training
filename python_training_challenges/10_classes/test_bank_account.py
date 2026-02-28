import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_initial_balance(self):
        account = BankAccount()
        self.assertEqual(account.get_balance(), 0)
        
    def test_deposit(self):
        account = BankAccount()
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)
        
    def test_withdraw(self):
        account = BankAccount()
        account.deposit(100)
        account.withdraw(30)
        self.assertEqual(account.get_balance(), 70)
        
    def test_withdraw_overdraft(self):
        account = BankAccount()
        account.deposit(50)
        account.withdraw(100)  # Should not allow overdraft
        self.assertEqual(account.get_balance(), 50)


if __name__ == "__main__":
    unittest.main()
