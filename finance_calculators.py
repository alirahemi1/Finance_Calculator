# Here we have compulsory task 1, a program for two financial calculators
# We have two strings with an input function for the user to choose from.
import math
investment = "investment - to calculate the amount of interest you'll earn on your investment"
bond = "bond - to calculate the amount you'll have to pay on a home loan"
print(investment)
print(bond)
user = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Here we have an if statement to choose either 'investment' or 'bond', it is not case-sensitive
# The rest are input functions
# I have used an empty print function at the end to give an extra space, making it look good aesthetically
if user.lower() == "investment":
    print("Please fill in the following details correctly: ")
    deposit = float(input("Please enter the deposit amount: "))
    interest_rate = float(input("Please enter the percentage for interest rate (only the number): "))
    years = float(input("Please enter the number of years for investing: "))
    print()

    # Here we have the variable interest, and we have an if statement inside an if statement
    # An if statement is to choose between 'simple' or 'compound'
    # It will print an error message if there is an incorrect input
    interest = input("Enter either 'simple' or 'compound' for interest type: ")
    if interest.lower() == "simple":
        print("You have selected simple interest.")
        simple_interest = deposit * (1 + (interest_rate/100) * years)
        print("Your simple interest is: ", simple_interest)

    elif interest.lower() == "compound":
        print("You have selected compound interest.")
        compound_interest = deposit * (1 + interest_rate/100) ** years
        print("Your compound  interest is: ", compound_interest)

    else:
        print("Wrong input. Please enter the correct input.")

# This elif statement will run if the first if statement is false
# We have the calculations for the repayment here too and printing the answer to the user
elif user.lower() == "bond":
    print("Please fill in the following details correctly: ")
    present_value = float(input("Please enter the current house value: "))
    interest_rate = float(input("Please enter the interest rate (only the numbers): "))
    months = int(input("Please enter the number of months for repayment: "))
    monthly_interest_rate = (interest_rate / 100) / 12
    monthly_payment = (monthly_interest_rate * present_value) / (1 - (1 + monthly_interest_rate) ** (-months))
    print("Monthly payment: {:.2f}".format(monthly_payment))

# An error message will run if an incorrect input is entered
else:
    print("Wrong input. Please enter the correct input.")
