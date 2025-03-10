import csv
from datetime import datetime
from turtle import pd
import unittest

class BankAccount:
    def __init__(self, account_number="", name="", checking_balance=0.0, savings_balance=0.0, overdraft_count=0, active=True, password=""):
        with open('bank.csv', 'r') as project:
            project = csv.reader(project)
            for i in project:
                print(i)
                
        self.account_number = account_number
        self.name = name
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
        self.overdraft_count = overdraft_count
        self.active = active
        self.password = password

    def get_account_details(self):
        return {
            'account_number': self.account_number,
            'name': self.name,
            'checking_balance': self.checking_balance,
            'savings_balance': self.savings_balance,
            'overdraft_count': self.overdraft_count,
            'active': self.active,
            'password': self.password
        }

    def withdraw(self, account_type, amount):
        if account_type == "checking":
            if self.checking_balance >= amount:
                self.checking_balance -= amount
                return True
        elif account_type == "savings":
            if self.savings_balance >= amount:
                self.savings_balance -= amount
                return True
        return False

    def deposit(self, account_type, amount):
        if account_type == "checking":
            self.checking_balance += amount
        elif account_type == "savings":
            self.savings_balance += amount
        return True

    def transfer(self, recipient_account, account_type, amount):
        if self.withdraw(account_type, amount):
            if account_type == "checking":
                recipient_account.deposit("checking", amount)
            elif account_type == "savings":
                recipient_account.deposit("savings", amount)
            return True
        return False

class Transaction:
    def __init__(self, account_number, transaction_type, amount, resulting_balance):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount
        self.resulting_balance = resulting_balance

    def get_transaction_details(self):
        return {
            'timestamp': self.timestamp,
            'account_number': self.account_number,
            'transaction_type': self.transaction_type,
            'amount': self.amount,
            'resulting_balance': self.resulting_balance
        }

def load_transactions(filename="transactions.csv"):
    try:
        df = pd.read_csv(filename)
        transactions = [Transaction(**row) for _, row in df.iterrows()]
        return transactions
    except FileNotFoundError:
        return []
    except pd.errors.EmptyDataError:
        return []

def save_transactions(transactions, filename="transactions.csv"):
    data = [t.get_transaction_details() for t in transactions]
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("12345", "Test User", 100, 50, password="testpass")
        self.bank = Bank()
        self.bank.add_account(self.account)

    def test_deposit(self):
        initial_balance = self.account.checking_balance
        self.account.deposit("checking", 50)
        self.assertEqual(self.account.checking_balance, initial_balance + 50)

    def test_withdraw(self):
        initial_balance = self.account.savings_balance
        self.account.withdraw("savings", 20)
        self.assertEqual(self.account.savings_balance, initial_balance - 20)

if __name__ == "__main__":
    unittest.main()
    BankAccount()
    Transaction()
    Bank()
    TestBankAccount()