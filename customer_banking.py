# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Hello. What is your savings account balance?"))
    savings_interest = float(input("Next, what is your annual interest rate?"))
    savings_maturity = int(input("Finally, what is the account's maturity (in months)?"))


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Here are your savings account details:")
    print("The interest earned on your account is: $", format(interest_earned, ",.2f"))
    print("Your updated savings account balance is: $", format(updated_savings_balance, ",.2f"))
    print("* Values based on interest earned for", savings_maturity, "months *")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Hello again. Now, what is your CD account balance?"))
    cd_interest = float(input("What is your annual CD interest rate?"))
    cd_maturity = int(input("Finally, what is the CD account's maturity (in months)?"))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Here are your CD account details:")
    print("The interest earned on your CD account is: $", format(interest_earned, ",.2f"))
    print("Your updated CD account balance is: $", format(updated_cd_balance, ",.2f"))
    print("* Values based on interest earned for", cd_maturity, "months *")

if __name__ == "__main__":
    # Call the main function.
    main()