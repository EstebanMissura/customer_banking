# customer_banking
Module 3 Challenge

By: Esteban Missura
Date: 6/2/2024

Brief Description:
1. This is a customer banking system that allows users to input their savings and CD account balances and then calculates and tracks interest earned on these accounts based on their maturity. It asks the users for the info, calculates and then prints the results. One thing to mention is that the assignment did not ask for error handling and messages, which is why I have not included that in my assignment submission. However, adding this to the assignment requirements would improve the code, and make the assignment more challenging and meaningful.

Detailed Description and Files
1. Accounts.py file
    * Contains the Account class with methods to set the balance and interest (given with the starter code).
2. Savings_account.py file
    * Imports the Accounts class, creates the create_savings_account function which creates the account, calculates the interest, updates the account balance, and returns both the interest earcned and the new balance (added my code to this file).
3. CD_account.py file
    * Much like the previous file (savings_account.py) but for the CD account. It imports the Accounts class, creates the create_cd_account function which creates the account, calculates the interest, updates the account balance, and returns both the interest earcned and the new balance (added my code to this file).
4. Customer_banking.py file
    * Imports both functions mentioned above (create_savings_account and create_cd_account), creates the main function which asks the user to enter their savings and CD account details, calls the corresponding functions to calculate the new balances and interests earned, and prints out the results (added my code to this file).
