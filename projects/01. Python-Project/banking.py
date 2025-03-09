import csv
import datetime
import os 



CUSTOMERS_FILE = "customers.csv"

class Bank:
    def _init_(self):
        self.customers = self.load_customers()

    def load_customers(self):
        """Load customer data from CSV."""
        if not os.path.exists(CUSTOMERS_FILE):
            return {}

        customers = {}
        with open(CUSTOMERS_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                customers[row["username"]] = {
                    "name": row["name"],
                    "password": row["password"],
                    "checking": float(row["checking"]),
                    "savings": float(row["savings"]),
                    "overdrafts": int(row["overdrafts"]),
                    "active": row["active"] == "True",
                }
        return customers

    def save_customers(self):
        """Save customer data to CSV."""
        with open(CUSTOMERS_FILE, mode="w", newline="") as file:
            fieldnames = ["username", "name", "password", "checking", "savings", "overdrafts", "active"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for username, data in self.customers.items():
                writer.writerow({
                    "username": username,
                    "name": data["name"],
                    "password": data["password"],
                    "checking": data["checking"],
                    "savings": data["savings"],
                    "overdrafts": data["overdrafts"],
                    "active": data["active"]
                })

    def add_customer(self, username, name, password, has_checking=True, has_savings=True):
        """Add a new customer."""
        if username in self.customers:
            return "Username already exists!"

        self.customers[username] = {
            "name": name,
            "password": password,
            "checking": 0.0 if has_checking else None,
            "savings": 0.0 if has_savings else None,
            "overdrafts": 0,
            "active": True
        }
        self.save_customers()
        return "Customer added successfully!"
    


class Auth:
    def _init_(self):
        self.bank = Bank()

    def login(self, username, password):
        """Authenticate user login."""
        if username in self.bank.customers:
            user = self.bank.customers[username]
            if user["password"] == password and user["active"]:
                return True
        return False
    
TRANSACTIONS_FILE = "transactions.csv"

class Transactions:
    def _init_(self):
        self.bank = Bank()
        self.overdraft = Overdraft(self.bank)

    def log_transaction(self, username, type, amount, balance):
        """Record transaction in CSV."""
        with open(TRANSACTIONS_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, datetime.datetime.now(), type, amount, balance])

    def deposit(self, username, account_type, amount):
        """Deposit money into checking or savings."""
        if amount <= 0:
            return "Invalid deposit amount!"
        
        user = self.bank.customers[username]
        if user[account_type] is None:
            return f"{account_type.capitalize()} account does not exist!"

        user[account_type] += amount
        self.bank.save_customers()
        self.log_transaction(username, "Deposit", amount, user[account_type])
        return "Deposit successful!"

    def withdraw(self, username, account_type, amount):
        """Withdraw money with overdraft protection."""
        user = self.bank.customers[username]
        return self.overdraft.process_withdrawal(username, account_type, amount)

    def transfer(self, from_user, to_user, from_account, amount):
        """Transfer money between accounts or to another customer."""
        if amount <= 0:
            return "Invalid transfer amount!"

        sender = self.bank.customers[from_user]
        recipient = self.bank.customers.get(to_user)

        if sender[from_account] is None or sender[from_account] < amount:
            return "Insufficient funds!"

        sender[from_account] -= amount
        if recipient:
            recipient["checking"] += amount  # All transfers go to checking by default
        else:
            return "Recipient not found!"

        self.bank.save_customers()
        self.log_transaction(from_user, "Transfer", amount, sender[from_account])
        return "Transfer successful!"
        
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
    

Bank()
Auth()
Transactions()
Overdraft()

