import csv
import os

seed_data = [
    {"account_id": 10001, "active": True, "first_name": "Nassir", "last_name": "Alhilal", "password": "234", "checking_balance": 200, "saving_balance": 200, "overdraft_count": 0 },
    {"account_id": 10002, "active": True, "first_name": "Nassir", "last_name": "Alhilal", "password": "234", "checking_balance": 200, "saving_balance": 300, "overdraft_count": 0 },
    {"account_id": 10003, "active": False, "first_name": "Nassir", "last_name": "Alhilal", "password": "234", "checking_balance": 200, "saving_balance": 100, "overdraft_count": 0 },
    {"account_id": 10004, "active": True, "first_name": "Nassir", "last_name": "Alhilal", "password": "234", "checking_balance": 200, "saving_balance": 5000, "overdraft_count": 0 },
    {"account_id": 10005, "active": True, "first_name": "Nassir", "last_name": "Alhilal", "password": "234", "checking_balance": 200, "saving_balance": 6000, "overdraft_count": 0 },
]

fieldnames = ["account_id", "active", "first_name", "last_name", "password", "checking_balance", "saving_balance", "overdraft_count"]

filename = "./bank.csv"

def setup_csv_file(filename, fieldnames):
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as csvfile:
            try:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in seed_data:
                    writer.writerow(row)
            except csv.Error as e:
                print(e)
                 
setup_csv_file(filename, fieldnames)

class Account:
    def __init__(self, row):
        self.account_id = row["account_id"]
        self.first_name = row["first_name"]
        self.last_name = row["last_name"]
        self.active = row["active"]
        self.password = row["password"]
        self.checking_balance = row["checking_balance"]
        self.saving_balance = row["saving_balance"]
        self.overdraft_count = row["overdraft_count"]
    
    def __str__(self):
        return f'"account_id {self.account_id}", "active {self.active}", "first_name {self.first_name}", "last_name {self.last_name}", "password {self.password}", "checking_balance {self.checking_balance}", "saving_balance {self.saving_balance}", "overdraft_count {self.overdraft_count}"'

    def deposit(self, account_type, amount):
        if account_type == "checking":
            self.checking_balance += amount
            return True
        elif account_type == "saving":
            self.saving_balance += amount
            return True
        return False

    def withdraw(self, account_type, amount):
            if account_type == "checking":
                if self.checking_balance - amount < -100:
                    print("Withdrawal denied. Account cannot have a balance less than -$100.")
                    return False
                if self.checking_balance < 0:
                    print("Withdrawal denied. Cannot withdraw more than $100 when account is negative.")
                    return False
                self.checking_balance -= amount
                if self.checking_balance < 0:
                    self.checking_balance -= 35  
                    self.overdraft_count += 1
                    if self.overdraft_count >= 2:
                        self.active = False
                        print("Account deactivated due to multiple overdrafts.")
                return True
            elif account_type == "savings":
                if self.saving_balance - amount < -100:
                    print("Withdrawal denied. Account cannot have a balance less than -$100.")
                    return False
                if self.saving_balance < 0:
                    print("Withdrawal denied. Cannot withdraw more than $100 when account is negative.")
                    return False
                self.saving_balance -= amount
                if self.saving_balance < 0:
                    self.saving_balance -= 35  
                    self.overdraft_count += 1
                    if self.overdraft_count >= 2:
                        self.active = False
                        print("Account deactivated due to multiple overdrafts.")
                return True
            return False

    def transfer(self, recipient_account, account_type, amount):
            if self.withdraw(account_type, amount):
                if account_type == "checking":
                    recipient_account.checking_balance += amount
                elif account_type == "savings":
                    recipient_account.saving_balance += amount
                return True
            return False

class Bank:
    id = 10001

    def __init__(self, bank):
        self.bank = bank
        self.customers = []
        # self.cus()
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def authenticate_user(self, account_number, password):
        for c in self.customers:
            if str(c.account_id) == account_number and c.password == password:
                return c
        return None
    
    def cus(self):
        with open("./bank.csv", 'w', newline='') as csvfile:
            acc_id = self.acc_id()
            acc_type = "checking"
            active = True
            first_name = "John"
            last_name = "Doe"
            password = "password123"
            checking_balance = 0.0
            saving_balance = 0.0
            saving_balance = 0.0
            overdraft_count = 0
            new_account = Account(acc_id, acc_type, active, first_name, last_name, password, checking_balance, saving_balance, overdraft_count)
            # self.customers.append(new_account)
            # fieldnames = ["account_id", "account_type", "first_name", "last_name", "password"]
            # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            # writer.writerow({"account_id": "", "account_type": "", "first_name": "", "last_name": "", "password": ""}) 
            try:
                new_account = Account(acc_id, acc_type, first_name, last_name, password)
                self.customers.append(new_account)
                fieldnames = ["account_id", "account_type", "first_name", "last_name", "password", "checking_balance", "saving_balance", "overdraft_count"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                # writer.writerow({"account_id": "", "account_type": "", "first_name": "", "last_name": "", "password": ""})
                for customer in self.customers:
                    writer.writerow({
                        "account_id": customer.account_id,
                        "account_type": customer.account_type,
                        "active": customer.active,
                        "first_name": customer.first_name,
                        "last_name": customer.last_name,
                        "password": customer.password,
                        "checking_balance": customer.checking_balance,
                        "saving_balance": customer.saving_balance,
                        "overdraft_count": customer.overdraft_count
                    })
            except csv.Error as e:
                print(f"CSV error: {e}")

    def save_customers(self):
            with open("./bank.csv", 'w', newline='') as csvfile:
                fieldnames = ["account_id", "active", "first_name", "last_name", "password", "checking_balance", "saving_balance", "overdraft_count"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for customer in self.customers:
                    writer.writerow({
                        "account_id": customer.account_id,
                        "active": customer.active,
                        "first_name": customer.first_name,
                        "last_name": customer.last_name,
                        "password": customer.password,
                        "checking_balance": customer.checking_balance,
                        "saving_balance": customer.saving_balance,
                        "overdraft_count": customer.overdraft_count
                    })
    def acc_id(self):
        if not self.customers:
            return 1001
        else:
            last_id = int(self.customers[-1].account_id)
            return last_id + 1

    def signup(self):
        print("Creating a new account.")
        first_name = input("enter your first name: ").strip().title()
        last_name = input("enter your last name: ").strip().title()
        password = input("enter your password: ").strip()
        print("choose account type:")
        print("1. checking")
        print("2. savings")
        print("3. both")
        acc_type = None
        while True:
            choice = input("enter choice (1/2/3): ")
            acc_type = {"1": "checking", "2": "savings", "3": "both"}.get(choice)
            if acc_type:
                break
            else:
                print("invalid choice. please select again.")
        acc_id = self.acc_id()
        new_account = Account(acc_id, acc_type, first_name, last_name, password)
        self.customers.append(new_account)
        self.save_customers()
        print(f"account created successfully, your account id is {acc_id}")

    def login(self):
        account_number = input("Enter your account number: ")
        password = input("Enter your password: ")
        account = self.authenticate_user(account_number, password)
        print(account)
        if account:
            print(f"Welcome back, {account.first_name} {account.last_name}!")
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
                Deposit(self)
                Deposit.deposit_money(self, account)
            elif choice == '3':
                Withdraw(self)
                Withdraw.withdraw_money(self, account)
            elif choice == '4':
                self.transfer_money(account)
            elif choice == '5':
                print("Logging out...")
                break
            else:
                print("Invalid choice, please try again.")

    def check_balance(self, account):
        print(f"\nAccount Balance:")
        print(f"Checking: ${account.checking_balance}")
        print(f"Savings: ${account.saving_balance}")

    def transfer_money(self, account):
        recipient_account_number = input("Enter recipient account number: ")
        recipient_account = next((customer for customer in self.customers if customer.account_id == int(recipient_account_number)), None)
        if recipient_account:
            account_type = input("Transfer from (checking/savings): ").lower()
            try:
                amount = float(input("Enter transfer amount: "))
                if amount <= 0:
                    print("Transfer amount must be positive.")
                    return
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                return
            if account.transfer(recipient_account, account_type, amount):
                print(f"Transferred ${amount:.2f} to account {recipient_account_number}.")
                self.save_customers()
            else:
                print("Transfer failed.")
        else:
            print("Recipient account not found.")

    def start(self):
        with open('./bank.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id = int(row['account_id'])
                row["account_id"] = int(row["account_id"])
                row['checking_balance'] = float(row["checking_balance"]) if row["checking_balance"] else 0.0
                row['saving_balance'] = float(row["saving_balance"]) if row["saving_balance"] else 0.0
                row['active'] = row['active'].lower() == 'true'
                self.customers.append(Account(row))

        print("Welcome to the Banking App!")
        while True:
            print("\n1. Login")
            print("2. Sign Up")
            print("3. Main Menu")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == '1':
                account = self.login()
                if account:
                    self.main_menu(account)
            elif choice == '2':
                self.signup()
            elif choice == '3':
                print("Please log in first to access the main menu.")
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

class Deposit(Bank):
        def deposit_money(self, account):
            account_type = input("Deposit to (checking/savings): ").lower()
            if account_type not in ["checking", "savings"]:
                print("Invalid account type. Please enter 'checking' or 'savings'.")
                return
            try:
                amount = float(input("Enter deposit amount: "))
                if amount <= 0:
                    print("Deposit amount must be positive.")
                    return
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                return
            if account.deposit(account_type, amount):
                print(f"Deposited ${amount:.2f} to {account_type} account.")
                self.save_customers()
            else:
                print("Deposit failed.")

class Withdraw(Bank):
        def withdraw_money(self, account):
            account_type = input("Withdraw from (checking/savings): ").lower()
            try:
                amount = float(input("Enter withdrawal amount: "))
                if amount <= 0:
                    print("Withdrawal amount must be positive.")
                    return
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                return
            if account_type == "checking" and account.checking_balance < amount:
                print("Insufficient balance for withdrawal.")
                return
            elif account_type == "savings" and account.saving_balance < amount:
                print("Insufficient balance for withdrawal.")
                return
            if account.withdraw(account_type, amount):
                print(f"Withdrew ${amount:.2f} from {account_type} account.")
                self.save_customers()
            else:
                print("Withdrawal failed.")

if __name__ == "__main__":
    bank_app = Bank("bank.csv")
    bank_app.start()