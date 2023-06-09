annual_salary = int(input("Enter your annual salary: "))
monthly_salary = annual_salary / 12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# assuming down payment is 25%
portion_down_payment = 0.25 * total_cost
# assuming current savings is 0
current_savings = 0
# assuming 4% annual return on investment
r = 0.04
# assuming 0 months have passed
months = 0
while current_savings < portion_down_payment:
    # salary increases every 6 months
    if months % 6 == 0 and months != 0:
        monthly_salary += monthly_salary * semi_annual_raise

    # assuming salary is deposited at the end of the month, interest is also calculated at the end of the month
    current_savings += (current_savings * (r / 12)) + (monthly_salary * portion_saved)
    months += 1

print("Number of months:", months)


