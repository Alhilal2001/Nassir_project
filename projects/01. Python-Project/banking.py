import csv
from datetime import datetime



class BankAccount:
    id = 1000

    def __init__(self, name, checking_balance, savings_balance, password, overdraft_count=0, active=True):
        BankAccount.id += 1
        self.account_number = BankAccount.id
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

    def authenticate_user(self, account_number, password):
        account = self.get_account(account_number)
        if account and account.password == password:
            return account
        return None

class BankingApp:
    def __init__(self):
        self.bank = Bank()

    def signup(self):
        print("Creating a new account.")
        account_number = input("Enter a new account number: ")
        name = input("Enter your full name: ")
        password = input("Create a password: ")
        checking_balance = float(input("Enter initial checking balance: "))
        savings_balance = float(input("Enter initial savings balance: "))
        account = BankAccount(account_number, name, checking_balance, savings_balance, password=password)
        self.bank.add_account(account)
        print(f"Account for {name} created successfully!")

    def login(self):
        account_number = input("Enter your account number: ")
        password = input("Enter your password: ")
        account = self.bank.authenticate_user(account_number, password)
        if account:
            print(f"Welcome back, {account.name}!")
            return account
        else:
            print("Invalid credentials. Please try again.")
            return None

    def main_menu(self, account):
        while True:
            print("\nMain Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transfer Money")
            print("5. Log out")
            choice = input("Choose an option (1-5): ")

            if choice == '1':
                self.check_balance(account)
            elif choice == '2':
                self.deposit_money(account)
            elif choice == '3':
                self.withdraw_money(account)
            elif choice == '4':
                self.transfer_money(account)
            elif choice == '5':
                print("Logging out...")
                break
            else:
                print("Invalid choice, please try again.")

    def check_balance(self, account):
        print(f"\nAccount Balance:")
        print(f"Checking: ${account.checking_balance:.2f}")
        print(f"Savings: ${account.savings_balance:.2f}")

    def deposit_money(self, account):
        account_type = input("Deposit to (checking/savings): ").lower()
        amount = float(input("Enter deposit amount: "))
        if account.deposit(account_type, amount):
            print(f"Deposited ${amount:.2f} to {account_type} account.")
        else:
            print("Deposit failed.")

    def withdraw_money(self, account):
        account_type = input("Withdraw from (checking/savings): ").lower()
        amount = float(input("Enter withdrawal amount: "))
        if account.withdraw(account_type, amount):
            print(f"Withdrew ${amount:.2f} from {account_type} account.")
        else:
            print("Insufficient balance for withdrawal.")

    def transfer_money(self, account):
        recipient_account_number = input("Enter recipient account number: ")
        recipient_account = self.bank.get_account(recipient_account_number)
        if recipient_account:
            account_type = input("Transfer from (checking/savings): ").lower()
            amount = float(input("Enter transfer amount: "))
            if account.transfer(recipient_account, account_type, amount):
                print(f"Transferred ${amount:.2f} to account {recipient_account_number}.")
            else:
                print("Transfer failed.")
        else:
            print("Recipient account not found.")

    def start(self):
        print("Welcome to the Banking App!")
        while True:
            print("\n1. Login")
            print("2. Sign Up")
            print("3. Exit")
            choice = input("Choose an option (1-3): ")

            if choice == '1':
                account = self.login()
                if account:
                    self.main_menu(account)
            elif choice == '2':
                self.signup()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = BankingApp()
    app.start()

