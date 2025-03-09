import csv
import datetime
from turtle
import unittest

class BankAccount:
    def __init__(self, account_number=0, name=0, checking_balance=0, savings_balance=0, overdraft_count=0, active=True, password=""):
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
        self.password=password

class Overdraft:
    OVERDRAFT_FEE = 35
    MAX_NEGATIVE_BALANCE = -100

    def _init_(self, bank):
        self.bank = bank

    def process_withdrawal(self, username, account_type, amount):
        """Handle withdrawals with overdraft protection."""
        user = self.bank.customers[username]
        balance = user[account_type]

        if balance - amount < self.MAX_NEGATIVE_BALANCE:
            return "Overdraft limit reached!"

        if balance < 0 and amount > 100:
            return "Cannot withdraw more than $100 when negative!"

        user[account_type] -= amount
        if user[account_type] < 0:
            user["overdrafts"] += 1
            user[account_type] -= self.OVERDRAFT_FEE

        if user["overdrafts"] >= 2:
            user["active"] = False  # Deactivate account

        self.bank.save_customers()
        return "Withdrawal successful!"

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

class Transaction:
    def _init_(self, account_number, transaction_type, amount, resulting_balance):
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

def add_customer(accounts):
    account_number = input("Enter account number: ")
    name = input("Enter customer name: ")
    password = input("Enter password: ")
    checking = input("Open checking account? (yes/no): ").lower() == "yes"
    savings = input("Open savings account? (yes/no): ").lower() == "yes"
    checking_balance = float(input("Enter initial checking balance: ") if checking else 0)
    savings_balance = float(input("Enter initial savings balance: ") if savings else 0)
    account = BankAccount(account_number, name, checking_balance, savings_balance, password=password)
    accounts[account_number] = account
    print("Customer added successfully.")
    
def login(self, username, password):
        """Authenticate user login."""
        if username in self.bank.customers:
            user = self.bank.customers[username]
            if user["password"] == password and user["active"]:
                return True
        return False

def withdraw_money(account, transactions):
    account_type = input("Withdraw from (checking/savings): ").lower()
    amount = float(input("Enter withdrawal amount: "))
    if account.withdraw(account_type, amount):
        balance = account.checking_balance if account_type == "checking" else account.savings_balance
        transactions.append(Transaction(account.account_number, f"Withdraw {account_type.capitalize()}", amount, balance))
        print("Withdrawal successful.")
    else:
        print("Withdrawal failed.")

def deposit_money(account, transactions):
    account_type = input("Deposit to (checking/savings): ").lower()
    amount = float(input("Enter deposit amount: "))
    if account.deposit(account_type, amount):
        balance = account.checking_balance if account_type == "checking" else account.savings_balance
        transactions.append(Transaction(account.account_number, f"Deposit {account_type.capitalize()}", amount, balance))
        print("Deposit successful.")
    else:
        print("Deposit failed.")

def transfer_money(account, accounts, transactions):
    recipient_account_number = input("Enter recipient account number: ")
    account_type = input("Transfer from (checking/savings): ").lower()
    amount = float(input("Enter transfer amount: "))
    if recipient_account_number in accounts and account.transfer(accounts[recipient_account_number], account_type, amount):
            balance = account.checking_balance if account_type == "checking" else account.savings_balance
            transactions.append(Transaction(account.account_number, f"Transfer {account_type.capitalize()} to {recipient_account_number}", amount, balance))
            print("Transfer successful.")
    else:
            print("Transfer failed.")

def display_transactions(account, transactions):
    account_transactions = [t for t in transactions if t.account_number == account.account_number]
    if account_transactions:
        print("\nTransaction History:")
        for transaction in account_transactions:
            print(f"  {transaction.timestamp} - {transaction.transaction_type}: ${transaction.amount:.2f}, Balance: ${transaction.resulting_balance:.2f}")
    else:
        print("No transactions found.")

def display_transaction_details(transactions):
    try:
        index = int(input("Enter transaction index (starting from 0): "))
        if 0 <= index < len(transactions):
            transaction = transactions[index]
            print(f"\nTransaction Details:")
            print(f"  Timestamp: {transaction.timestamp}")
            print(f"  Account Number: {transaction.account_number}")
            print(f"  Transaction Type: {transaction.transaction_type}")
            print(f"  Amount: ${transaction.amount:.2f}")
            print(f"  Resulting Balance: ${transaction.resulting_balance:.2f}")
        else:
            print("Invalid transaction index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("12345", "Test User", 100, 50, password="testpass")


BankAccount()
Overdraft()
Transaction()
TestBankAccount()

## How is a user going to interact with you app? Is the progam going to start with an input? IS it going to be like a chatbot?

## at what point of the program, wil they have the choice to sign in, or withdraw

## have some main function that begins the interaction with the customer
#treat the user like a customer 