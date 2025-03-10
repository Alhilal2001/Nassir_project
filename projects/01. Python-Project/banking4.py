import csv
import os
import re
from datetime import datetime

CUSTOMER_FILE = "customers.csv"
TRANSACTION_FILE = "transactions.csv"
OVERDRAFT_FEE = 35
MAX_NEGATIVE_BALANCE = -100

# Ensure CSV files exist
def initialize_files():
    if not os.path.exists(CUSTOMER_FILE):
        with open(CUSTOMER_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Checking", "Savings", "Overdrafts", "Status"])
    
    if not os.path.exists(TRANSACTION_FILE):
        with open(TRANSACTION_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Customer ID", "Date", "Time", "Type", "Amount", "Balance"])

# Load customers from CSV
def load_customers():
    customers = {}
    with open(CUSTOMER_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            customers[row["ID"]] = {
                "name": row["Name"],
                "checking": float(row["Checking"]),
                "savings": float(row["Savings"]),
                "overdrafts": int(row["Overdrafts"]),
                "status": row["Status"]
            }
    return customers

# Save customers to CSV
def save_customers(customers):
    with open(CUSTOMER_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Checking", "Savings", "Overdrafts", "Status"])
        for cid, data in customers.items():
            writer.writerow([cid, data["name"], data["checking"], data["savings"], data["overdrafts"], data["status"]])

# Record a transaction
def record_transaction(cid, transaction_type, amount, balance):
    now = datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
    with open(TRANSACTION_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([cid, *now.split(","), transaction_type, amount, balance])

# Add a new customer
def add_customer():
    name = input("Great! What's your full name? ").strip().title()
    account_type = input("Would you like a checking account, savings account, or both? ").lower().strip()
    customers = load_customers()
    cid = str(len(customers) + 1)  # Simple auto-increment ID
    checking = 0.0 if "checking" in account_type else None
    savings = 0.0 if "savings" in account_type else None
    customers[cid] = {"name": name, "checking": checking or 0, "savings": savings or 0, "overdrafts": 0, "status": "Active"}
    save_customers(customers)
    print(f"\nWelcome, {name}! Your account has been created successfully. Your Customer ID is {cid}.\n")

# Deposit money
def deposit(cid, account, amount):
    customers = load_customers()
    if cid not in customers or customers[cid]["status"] != "Active":
        print("Invalid or inactive account.")
        return
    customers[cid][account] += amount
    save_customers(customers)
    record_transaction(cid, f"Deposit to {account}", amount, customers[cid][account])
    print(f"Deposited ${amount} into {account}. New balance: ${customers[cid][account]}.\n")

# Withdraw money
def withdraw(cid, account, amount):
    customers = load_customers()
    if cid not in customers or customers[cid]["status"] != "Active":
        print("Invalid or inactive account.")
        return

    balance = customers[cid][account]
    if balance - amount < MAX_NEGATIVE_BALANCE:
        print("Withdrawal exceeds allowed overdraft limit.")
        return

    customers[cid][account] -= amount
    if customers[cid][account] < 0:
        customers[cid][account] -= OVERDRAFT_FEE
        customers[cid]["overdrafts"] += 1
        print(f"Overdraft! A fee of ${OVERDRAFT_FEE} has been applied.")

        if customers[cid]["overdrafts"] >= 2:
            customers[cid]["status"] = "Inactive"
            print("Your account has been deactivated due to excessive overdrafts.")

    save_customers(customers)
    record_transaction(cid, f"Withdraw from {account}", amount, customers[cid][account])
    print(f"Withdrew ${amount} from {account}. New balance: ${customers[cid][account]}.\n")

# Display transactions
def display_transactions(cid):
    with open(TRANSACTION_FILE, "r") as f:
        reader = csv.DictReader(f)
        transactions = [row for row in reader if row["Customer ID"] == cid]

    if not transactions:
        print("No transactions found.\n")
        return

    print(f"\nTransaction history for Customer {cid}:")
    for txn in transactions:
        print(f"{txn['Date']} {txn['Time']} | {txn['Type']} | Amount: ${txn['Amount']} | Balance: ${txn['Balance']}")
    print()

# Main chatbot function
def start_chatbot():
    print("\n🌟 Welcome to ACME Bank! 🌟")
    print("How can I assist you today?\n")

    while True:
        user_input = input("> ").lower().strip()

        if "open account" in user_input or "create account" in user_input:
            add_customer()

        elif "deposit" in user_input:
            match = re.search(r"deposit (\d+) into (checking|savings)", user_input)
            if match:
                cid = input("Enter your Customer ID: ")
                amount = float(match.group(1))
                account = match.group(2)
                deposit(cid, account, amount)
            else:
                print("Please specify an amount and account type. Example: 'Deposit 500 into checking'")

        elif "withdraw" in user_input:
            match = re.search(r"withdraw (\d+) from (checking|savings)", user_input)
            if match:
                cid = input("Enter your Customer ID: ")
                amount = float(match.group(1))
                account = match.group(2)
                withdraw(cid, account, amount)
            else:
                print("Please specify an amount and account type. Example: 'Withdraw 200 from savings'")

        elif "show transactions" in user_input or "transaction history" in user_input:
            cid = input("Enter your Customer ID: ")
            display_transactions(cid)

        elif "exit" in user_input:
            print("\nThank you for banking with ACME Bank! We appreciate your trust. Have a wonderful day! 😊")
            break

        else:
            print("\nI'm here to assist you! You can say things like:")
            print("- 'Open an account'")
            print("- 'Deposit 500 into checking'")
            print("- 'Withdraw 200 from savings'")
            print("- 'Show my transaction history'")
            print("- 'Exit'\n")

# Run chatbot
if __name__ == "_main_":
    initialize_files()
    start_chatbot()
    