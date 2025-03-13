Banking Application
This is a simple banking application built using Python. The app allows users to create an account, log in, check balances, deposit and withdraw money, and transfer funds. It also handles overdrafts, account deactivation after multiple overdrafts, and saving account details in a CSV file.

Features
User Authentication: Allows users to sign up, log in, and access their account details.
Account Management: Create new accounts with either a checking or savings account type (or both).
Deposit and Withdrawal: Users can deposit and withdraw money from their checking or savings accounts.
Transfer Funds: Users can transfer money between accounts.
Overdraft Protection: Ensures accounts cannot go below -$100, with penalties for overdrafts and automatic deactivation after two overdrafts.
CSV Storage: Account details are saved and loaded from a CSV file, allowing the application to persist user data.
Requirements
Python 3.x
csv module (included in Python's standard library)
Setup
To run the application, clone the repository and navigate to the project directory.

bash
Copy code
git clone https://github.com/Nassir/banking-app.git
cd banking-app
No additional dependencies need to be installed, as everything is built with Python's standard library.

Usage
To start the banking application, simply run the banking_app.py script:

bash
Copy code
python banking_app.py
Main Menu
After logging in or signing up, the following menu will be displayed:

pgsql
Copy code
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Log out
Choose an option to interact with your bank account.

Account Types
You can choose between:

Checking Account: Allows you to perform transactions such as deposits, withdrawals, and transfers.
Savings Account: Similar to the checking account but intended for long-term savings.
Handling Overdrafts
If you attempt to withdraw more than the available balance, an overdraft fee of $35 will be applied. After two overdrafts, the account will be deactivated.

File Structure
bank.csv: A CSV file that stores all account data.
banking_app.py: The main Python script containing the banking logic and user interface.
Functions
setup_csv_file(filename, fieldnames)
Creates a CSV file with the initial seed data if the file does not already exist.

Account Class
Represents a bank account, with methods for depositing, withdrawing, and transferring money.

deposit(account_type, amount): Deposits money into the specified account type (checking or savings).
withdraw(account_type, amount): Withdraws money from the specified account type (checking or savings).
transfer(recipient_account, account_type, amount): Transfers money to another account.
Bank Class
Manages the bank operations, including user authentication, account creation, and account management.

add_account(account): Adds a new account to the bank.
authenticate_user(account_number, password): Authenticates a user based on their account number and password.
signup(): Allows users to create a new account.
login(): Authenticates users and grants access to their account.
main_menu(account): Displays the main menu after login, allowing users to check their balance, deposit, withdraw, or transfer funds.
Limitations
The application currently only supports a single CSV file (bank.csv) to store all account data.
There is no persistent session management; users must log in every time the application starts.
The overdraft logic and penalties are limited to the hard-coded rules within the application.
Contributing
Feel free to fork the repository and submit pull requests. If you find any issues or have feature requests, please open an issue.

License
- [Pretty-print tabular data in Python, a library and a command-line utility](https://pypi.org/project/tabulate/)
- [Command line colors](https://pypi.org/project/termcolor/)
- [Command line menu](https://pypi.org/project/simple-term-menu/)
