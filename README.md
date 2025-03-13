<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

![gif](https://media2.giphy.com/media/y3B74VeWI2QQE/giphy.gif)

**CHECK THE PROJECT FOLDER FOR THE ACTUAL PROJECT FILES**

# Banking With Python

In the third week of this course we worked through the fundamentals of working with Python Programming Language. This project is going to put those skills to test and challenge you to figure out how to use those skills to build a miniature version of a banking system. As usual, try your best to work through solving the problem on your own. The code in this project should be your own. If you do need help, please do not go to ChatGPT and get random code because this is a graded project. Ask your intructors for help or work through it on your own.

## Prompt

ACME Bank uses a file structure called `bank.csv`. The cashiers will use this brand-new software to manage transactions, and you have been tasked with developing it.

## Requirements

Your banking program should include the following:

- GitHub Repository:
  - Minimum 1 commit per day / 5 commits minimum overall.
  - one bank.csv file (provided);
  - one python file with all code
  - README.md file with:
    - project name and description
    - a table of app functionality / user stories (already provided)
    - technologies used
    - Icebox Features (other cool functionality you could add)
    - Challenges / Key Takeaways From Experience
    - dont be afraid to make it colorful and fun! Give it life :joy:
  
- Application Features:
  - 4 classes (minimum)
  - 1 file: `bank.csv`
  - 1 file: `banking.py`
  - 1 package: `csv`
    - **`import csv` at the top of your python file**
  - Unit Testing Based on **test-driven development (TDD)** approach
  - Functionality:
    - Add New Customer
        * customer can have a checking account
        * customer can have a savings account
        * customer can have both a checking and a savings account
    - Withdraw Money from Account (required login)
        * withdraw from savings
        * withdraw from checking
    - Deposit Money into Account (required login)
        * can deposit into savings
        * can deposit into checking
    - Transfer Money Between Accounts (required login)
        * can transfer from savings to checking
        * can transfer from checking to savings
        * can transfer from checking or savings to another customer's account
    - Build Overdraft Protection
        * charge customer ACME overdraft protection fee of $35 when overdraft
        * prevent customer from withdrawing more than $100 USD if account is currently negative
            * _the account cannot have a resulting balance of less than -$100_
              OR
            * _the customer cannot make a withdrawal of greater than $100_
        * deactivate the account after 2 overdrafts
            * reactivate the account if the customer brings the account current, paying both the overdraft amount and the
              resulting overdraft fees
    - **BONUS**
      - Display Transaction Data (You need to create another file to store the transaction history, required login)
      - index all transactions for a customer account
      - show one transaction **details**
      - show historical data of transactions (date and time of transaction, type of transaction, resulting balance, etc.)

**YOU WILL NEED TO USE THE PYTHON CSV PACKAGE TO WORK WITH THE BANK.CSV FILE**
**[PYTHON CSV](https://docs.python.org/3/library/csv.html)**


## EXAMPLES

```text
10001;suresh;sigera;juagw362;1000,10000
10002;james;taylor;idh36%@#FGd;10000,10000
10003;melvin;gordon;uYWE732g4ga1;2000,20000
10004;stacey;abrams;DEU8_qw3y72$;2000,20000
10005;jake;paul;d^dg23g)@;100000,100000
```

| account_id | frst_name | last_name | password    | balance_checking | balance_savings |
|------------|-----------|-----------|-------------|------------------|-----------------|
| 10001      | suresh    | sigera    | juagw362    | 1000             | 10000           | 
| 10002      | james     | taylor    | idh36%@#FGd | 10000            | 10000           |
| ...        | ...       | ...       | ...         | ...              | ...             |

Given the above file structure for the ACME Bank, write the entire Python program using classes, methods, file handling, and exception handling to meet the functional requirements below:


### Self-sufficiency / Project assistance

- At this stage being able to find the answers to development issues is of paramount importance.
- Use all resources available to solve the issue on your own before seeking assistance. (Please do not just copy and paste code from random sources)
- If you do seek assistance in Slack, use the support channel and explain the issue as clearly and detailed as you can,
  include screenshots when possible, and be prepared to explain what you've done to solve the issue on your own.

## Get started!

![gif](https://media.giphy.com/media/ADgfsbHcS62Jy/giphy.gif)

## Additional resources:

- [Pretty-print tabular data in Python, a library and a command-line utility](https://pypi.org/project/tabulate/)
- [Command line colors](https://pypi.org/project/termcolor/)
- [Command line menu](https://pypi.org/project/simple-term-menu/)
