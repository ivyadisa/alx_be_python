# Ask for user input
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly and annual savings
monthly_savings = income - expenses
annual_savings = monthly_savings * 12

# Use compound interest (5% annual)
projected_savings = annual_savings * 1.05

# Output results with 2 decimal places
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
