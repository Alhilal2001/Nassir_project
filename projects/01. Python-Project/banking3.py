import csv
from turtle import pd

class BankAccount:
    def _init_(self, account_number, name, balance, overdraft_count=0, active=True):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.overdraft_count = overdraft_count
        self.active = active

    def deposit(self, amount):
        if self.active:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if self.active:
            if self.balance >= amount:
                self.balance -= amount
                return True
            elif self.overdraft_count < 2:
                self.balance -= amount
                self.overdraft_count += 1
                if self.overdraft_count == 2:
                    self.active = False
                return True
            else:
                return False
        else:
            return False

    def transfer(self, recipient_account, amount):
        if self.active and recipient_account.active:
            if self.balance >= amount:
                self.balance -= amount
                recipient_account.deposit(amount)
                return True
            elif self.overdraft_count < 2:
                self.balance -= amount
                recipient_account.deposit(amount)
                self.overdraft_count += 1
                if self.overdraft_count == 2:
                    self.active = False
                return True
            else:
                return False
        else:
            return False

    def get_account_details(self):
        return {
            'account_number': self.account_number,
            'name': self.name,
            'balance': self.balance,
            'overdraft_count': self.overdraft_count,
            'active': self.active
        }

def load_accounts(filename="bank.csv"):
    try:
        df = pd.read_csv(filename)
        accounts = {}
        for index, row in df.iterrows():
            account = BankAccount(
                row['account_number'],
                row['name'],
                row['balance'],
                row['overdraft_count'],
                row['active']
            )
            accounts[row['account_number']] = account
        return accounts
    except FileNotFoundError:
        return {}
    except pd.errors.EmptyDataError:
        return {}

def save_accounts(accounts, filename="bank.csv"):
    data = []
    for account in accounts.values():
        data.append(account.get_account_details())
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def add_customer(accounts):
    account_number = input("Enter account number: ")
    name = input("Enter customer name: ")
    balance = float(input("Enter initial balance: "))
    account = BankAccount(account_number, name, balance)
    accounts[account_number] = account
    print("Customer added successfully.")

def withdraw_money(accounts):
    account_number = input("Enter account number: ")
    amount = float(input("Enter withdrawal amount: "))
    if account_number in accounts:
        if accounts[account_number].withdraw(amount):
            print("Withdrawal successful.")
        else:
            print("Withdrawal failed. Insufficient funds or account deactivated.")
    else:
        print("Account not found.")

def deposit_money(accounts):
    account_number = input("Enter account number: ")
    amount = float(input("Enter deposit amount: "))
    if account_number in accounts:
        if accounts[account_number].deposit(amount):
            print("Deposit successful.")
        else:
            print("Account deactivated.")
    else:
        print("Account not found.")

def transfer_money(accounts):
    source_account_number = input("Enter source account number: ")
    recipient_account_number = input("Enter recipient account number: ")
    amount = float(input("Enter transfer amount: "))
    if source_account_number in accounts and recipient_account_number in accounts:
        if accounts[source_account_number].transfer(accounts[recipient_account_number], amount):
            print("Transfer successful.")
        else:
            print("Transfer failed. Insufficient funds, or one or both accounts are deactivated.")
    else:
        print("One or both accounts not found.")

def main():
    accounts = load_accounts()
    while True:
        print("\nBanking System")
        print("1. Add Customer")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Transfer Money")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_customer(accounts)
        elif choice == "2":
            withdraw_money(accounts)
        elif choice == "3":
            deposit_money(accounts)
        elif choice == "4":
            transfer_money(accounts)
        elif choice == "5":
            save_accounts(accounts)
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__=="_main_":
    main()
