import csv
from datetime import datetime

# Overdraft Protection constants
OVERDRAFT_FEE = 35
MAX_NEGATIVE_BALANCE = -100

# BankAccount class to manage individual customer accounts
class BankAccount:
    def __init__(self, account_id, first_name, last_name, password, balance_checking=0.0, balance_savings=0.0, overdraft_count=0, active=True):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking_balance = balance_checking
        self.savings_balance = balance_savings
        self.overdraft_count = overdraft_count
        self.active = active

    def get_account_details(self):
        return {
            'account_id': self.account_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password,
            'checking_balance': self.checking_balance,
            'savings_balance': self.savings_balance,
            'overdraft_count': self.overdraft_count,
            'active': self.active
        }

    def withdraw(self, account_type, amount):
        """Withdraw from checking or savings account."""
        if self.active:
            if account_type == "checking" and self.checking_balance >= amount:
                self.checking_balance -= amount
                return True
            elif account_type == "savings" and self.savings_balance >= amount:
                self.savings_balance -= amount
                return True
        return False

    def deposit(self, account_type, amount):
        """Deposit into checking or savings account."""
        if account_type == "checking":
            self.checking_balance += amount
        elif account_type == "savings":
            self.savings_balance += amount
        return True

    def transfer(self, recipient_account, account_type, amount):
        """Transfer from checking or savings to another account."""
        if self.withdraw(account_type, amount):
            if account_type == "checking":
                recipient_account.deposit("checking", amount)
            elif account_type == "savings":
                recipient_account.deposit("savings", amount)
            return True
        return False

    def process_overdraft(self):
        """Process overdraft fee and deactivation."""
        if self.checking_balance < 0 or self.savings_balance < 0:
            if self.checking_balance < 0:
                self.checking_balance -= OVERDRAFT_FEE
            elif self.savings_balance < 0:
                self.savings_balance -= OVERDRAFT_FEE
            self.overdraft_count += 1

        if self.overdraft_count >= 2:
            self.active = False  # Account is deactivated after two overdrafts

# Transaction class to store transaction data
class Transaction:
    def __init__(self, account_id, transaction_type, amount, resulting_balance):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.resulting_balance = resulting_balance

    def get_transaction_details(self):
        return {
            'timestamp': self.timestamp,
            'account_id': self.account_id,
            'transaction_type': self.transaction_type,
            'amount': self.amount,
            'resulting_balance': self.resulting_balance
        }

# Bank class to manage multiple customer accounts
class Bank:
    def __init__(self, bank_file='bank.csv'):
        self.bank_file = bank_file
        self.accounts = {}

    def load_accounts(self):
        accounts = {}
        try:
            with open(self.bank_file, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    account_id, first_name, last_name, password, checking_balance, savings_balance, overdraft_count, active = row
                    accounts[account_id] = BankAccount(
                        account_id, first_name, last_name, password,
                        float(checking_balance), float(savings_balance),
                        int(overdraft_count), active.lower() == 'true'
                    )
        except FileNotFoundError:
            print("No existing bank data found. Starting fresh.")
        self.accounts = accounts
        return self.accounts

    def save_accounts(self):
        """Save all accounts to the bank CSV file."""
        with open(self.bank_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for account in self.accounts.values():
                writer.writerow([account.account_id, account.first_name, account.last_name, account.password,
                                 account.checking_balance, account.savings_balance, account.overdraft_count, account.active])

    def add_account(self, account):
        """Add new account to the bank."""
        self.accounts[account.account_id] = account
        self.save_accounts()

    def get_account(self, account_id):
        """Get account by account_id."""
        return self.accounts.get(account_id)

# BankApp to handle user interaction
class BankApp:
    def __init__(self, bank):
        self.bank = bank

    def sign_in(self, account_id, password):
        """Authenticate customer by account_id and password."""
        account = self.bank.get_account(account_id)
        if account and account.password == password and account.active:
            return account
        return None

    def add_new_customer(self):
        """Add a new customer to the bank."""
        account_id = input("Enter account ID: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        password = input("Enter password: ")
        checking_balance = float(input("Enter initial checking balance: "))
        savings_balance = float(input("Enter initial savings balance: "))

        new_account = BankAccount(account_id, first_name, last_name, password, checking_balance, savings_balance)
        self.bank.add_account(new_account)
        print(f"Account created for {first_name} {last_name}")

    def withdraw_money(self, account):
        """Withdraw money from a customer's account."""
        account_type = input("Withdraw from (checking/savings): ").lower()
        amount = float(input("Enter withdrawal amount: "))
        if account.withdraw(account_type, amount):
            print(f"Successfully withdrew ${amount:.2f} from {account_type} account.")
        else:
            print(f"Failed to withdraw from {account_type} account. Insufficient funds or inactive account.")

    def deposit_money(self, account):
        """Deposit money into a customer's account."""
        account_type = input("Deposit into (checking/savings): ").lower()
        amount = float(input("Enter deposit amount: "))
        account.deposit(account_type, amount)
        print(f"Successfully deposited ${amount:.2f} into {account_type} account.")

    def transfer_money(self, account):
        """Transfer money between customer accounts."""
        recipient_id = input("Enter recipient account ID: ")
        recipient_account = self.bank.get_account(recipient_id)
        if recipient_account:
            account_type = input("Transfer from (checking/savings): ").lower()
            amount = float(input("Enter transfer amount: "))
            if account.transfer(recipient_account, account_type, amount):
                print(f"Successfully transferred ${amount:.2f} to account {recipient_id}.")
            else:
                print("Transfer failed. Insufficient funds or invalid account type.")
        else:
            print("Recipient account not found.")
