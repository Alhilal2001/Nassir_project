# - 1 package: `csv`
#     - **`import csv` at the top of your python file**
#   - Functionality:
#     - Add New Customer
#         * customer can have a checking account
#         * customer can have a savings account
#         * customer can have both a checking and a savings account
#     - Withdraw Money from Account (required login)
#         * withdraw from savings
#         * withdraw from checking
#     - Deposit Money into Account (required login)
#         * can deposit into savings
#         * can deposit into checking
#     - Transfer Money Between Accounts (required login)
#         * can transfer from savings to checking
#         * can transfer from checking to savings
#         * can transfer from checking or savings to another customer's account
#     - Build Overdraft Protection
#         * charge customer ACME overdraft protection fee of $35 when overdraft
#         * prevent customer from withdrawing more than $100 USD if account is currently negative
#             * _the account cannot have a resulting balance of less than -$100_
#               OR
#             * _the customer cannot make a withdrawal of greater than $100_
#         * deactivate the account after 2 overdrafts
#             * reactivate the account if the customer brings the account current, paying both the overdraft amount and the
#               resulting overdraft fees
#     - **BONUS**
#       - Display Transaction Data (You need to create another file to store the transaction history, required login)
#       - index all transactions for a customer account
#       - show one transaction **details**
#       - show historical data of transactions (date and time of transaction, type of transaction, resulting balance, etc.)
#       - Unit Testing Based on **test-driven development (TDD)** approach

class bank:



# **YOU WILL NEED TO USE THE PYTHON CSV PACKAGE TO WORK WITH THE BANK.CSV FILE**
# **[PYTHON CSV](https://docs.python.org/3/library/csv.html)**


# ## EXAMPLES

# ```text
# 10001;suresh;sigera;juagw362;1000,10000
# 10002;james;taylor;idh36%@#FGd;10000,10000
# 10003;melvin;gordon;uYWE732g4ga1;2000,20000
# 10004;stacey;abrams;DEU8_qw3y72$;2000,20000
# 10005;jake;paul;d^dg23g)@;100000,100000
# ```

# | account_id | frst_name | last_name | password    | balance_checking | balance_savings |
# |------------|-----------|-----------|-------------|------------------|-----------------|
# | 10001      | suresh    | sigera    | juagw362    | 1000             | 10000           | 
# | 10002      | james     | taylor    | idh36%@#FGd | 10000            | 10000           |
# | ...        | ...       | ...       | ...         | ...              | ...             |

# Given the above file structure for the ACME Bank, write the entire Python program using classes, methods, file handling, and exception handling to meet the functional requirements below:
class bank:
    