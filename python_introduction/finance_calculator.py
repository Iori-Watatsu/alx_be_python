# This takes user input and calculates their monthly and potential future saving.

# These variables prompts for user's monthy income and total monthly expenses.
monthly_income = int(input("Enter your monthly income: " ))
monthly_expenses = int(input("Enter your monthly expenses: " ))

# This variable calulates user's monthly savings.
monthly_savings = monthly_income - monthly_expenses

# This variable calulates user's projected annual savings.
projected_savings = monthly_savings * 12 + int(monthly_savings * 12 * 0.05)

# Print the user's monthly savings.
print(f"Your monthly savings are ${monthly_savings}.")
# Print the user's projected annual savings.
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
