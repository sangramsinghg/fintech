'''
Challenge 1 Code

This code automates the process of valuing loans.
Author: Sangram Singh (Berkeley FinTech Team provided the starter code)

'''
# coding: utf-8
import csv
from pathlib import Path

# Define the annual discount rate variable that is used in the Present Value calculations
annual_discount_rate = 0.20

# Define a function that will be used to calculate monthly componded present value.
#    This function includes parameters for `future_value`, `remaining_months`,
#    and the `annual_discount_rate`
#
#    Monthly Compounded Present Value = Future Value / ((1 + (Annual Discount Rate/12)) ** Remaining Months)
#
#    The function returns the `present_value` for the loan.
def calculate_monthly_compounded_present_value(future_value, remaining_months, annual_discount_rate):
    monthly_compounded_present_value = future_value/((1 + (annual_discount_rate/12)) ** remaining_months)
    return monthly_compounded_present_value

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

print("Part 1 - LOAN SUMMARY CALCULATIONS\n")
# How many loans are in the list?
# Use the `len` function to calculate the total number of loans in the list.
total_number_of_loans = len(loan_costs)

# Print the number of loans from the list
print(f"a) Total number of loans under consideration are          : {total_number_of_loans}")

# What is the total of all loans?
# Use the `sum` function to calculate the total of all loans in the list.
total_value_of_loans = sum(loan_costs)

# Print the total value of the loans - 2 decimal places
print(f"b) Total value of the loans under consideration is        : ${total_value_of_loans:,.2f}")

# What is the average loan amount from the list?
# Using the sum of all loans and the total number of loans, calculate the average loan price.
average_loan_amount = total_value_of_loans / total_number_of_loans

# Print the average loan amount - 2 decimal places
print(f"c) Average Loan Amount of loans under consideration is    : ${average_loan_amount:,.2f}\n")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for 
what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and 
**Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20%
as the discount rate.

3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is 
    worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is 
    too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to 
    buy the loan at its current cost?
"""

# Given the following loan data, calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use get() on the dictionary of additional information to extract the Future Value, Loan Price 
# and Remaining Months on the loan.

remaining_months = loan.get("remaining_months")
future_value = loan.get("future_value")
loan_price = loan.get("loan_price")

print("Part 2 - PRESENT VALUE CALCULATION AND BUY RECOMMENDATION\n")
# Print each variable.
print(f"a) Remaining months of the loan are        : {remaining_months}")
print(f"b) Future value of the loan is             : ${future_value:,.2f}")
print(f"c) Loan price is                           : ${loan_price:,.2f}")

# We use the formula for Monthly Version of the Present Value to calculate a "fair value" of the loan.
# We use a minimum required return of 20% as the discount rate.
# We use the pre-defined function to calculate the monthly compounded present value
present_value = calculate_monthly_compounded_present_value(future_value, remaining_months, annual_discount_rate)
print(f"d) The Present (Fair) value of the loan is : ${present_value:,.2f}\n")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# Writing a conditional statement (an if-else statement) to decide if the present value 
# represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, 
#           then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost,
#           then print a message that says that the loan is too expensive and not worth the price.

if present_value >= loan_price:
    print("e) Recommend this loan! - The loan is worth at least the cost to buy it\n")
else:
    print("e) Do Not Recommend this loan! - loan is too expensive and not worth the price\n")

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# NOTE: The annual discount rate has been defined up front as a global
present_value = calculate_monthly_compounded_present_value(
            new_loan["future_value"],
            new_loan["remaining_months"],
            annual_discount_rate)

print("Part 3 - THE PRESENT VALUE OF A NEW LOAN\n")
print(f"The present value of the new loan is: ${present_value:,.2f}\n")

"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select 
only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan.get("loan_price") <= 500:
        inexpensive_loans.append(loan)

# Print the `inexpensive_loans` list as a python list
# The Inexpensive loans are the ones whose cost is <= $500.00
print("Part 4 - INEXPENSIVE LOANS (loan price or cost <= $500.00)\n") 
print("a) In the Python List Form :")
print(inexpensive_loans)

# Print the `inexpensive_loans` list as a more user friendly human readable output
print("\nb) In a User Friendly Form :")
# initialize the loan number to 1. This will be used to mark the list item appropriately
inexpensive_loan_number = 1
# iterate through all the inexpensive loans
for inexpensive_loan in inexpensive_loans:
    # print the loan number
    print(f"Loan # {inexpensive_loan_number}:")
    # iterate through all the dictionary items and print the key, value pair associated with the item
    for key, value in inexpensive_loan.items():
        print(f"    {key:<20s} : {value}")
    # increment the loan number
    inexpensive_loan_number += 1

"""Part 5: Save the results to a csv file.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Please Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, "w", newline='') as csv_file:
    # set the csv write to delimit the values with ","
    csv_writer = csv.writer(csv_file, delimiter=",")
    # write the header for the output
    csv_writer.writerow(header)
    # iterate through all the values in the `inexpensive_loans` and write them to the csv file
    for inexpensive_loan in inexpensive_loans:
        csv_writer.writerow(inexpensive_loan.values())