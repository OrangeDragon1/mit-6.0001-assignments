annual_salary = int(input("Enter your annual salary: "))

min_rate = 0
max_rate = 10000
portion_saved = max_rate // 2

# assuming 1,000,000 is the total cost of the house
total_cost = 1000000
# assuming 7% semi-annual raise
semi_annual_raise = .07
# assuming 4% annual return on investment
r = 0.04
# assuming down payment is 25%
portion_down_payment = 0.25 * total_cost
# assuming current savings is 0
current_savings = 0
# assuming 0 months have passed
months = 0
# bisection search counter
bisection_count = 0

if annual_salary * 3 < portion_down_payment:
    print("It is not possible to pay the down payment in three years.")
    exit()

while True:
    bisection_count += 1
    # reset current_savings to 0
    current_savings = 0
    # reset months to 0
    months = 0
    # reset monthly_salary to annual_salary / 12
    monthly_salary = annual_salary / 12
    while months < 36:
        # salary increases every 6 months
        if months % 6 == 0 and months != 0:
            monthly_salary += monthly_salary * semi_annual_raise

        # assuming salary is deposited at the end of the month, interest is also calculated at the end of the month
        current_savings += (current_savings * (r / 12)) + (monthly_salary * (portion_saved / 10000))
        months += 1

    if abs(current_savings - portion_down_payment) <= 100:
        break

    if current_savings < portion_down_payment:
        min_rate = portion_saved
    else:
        max_rate = portion_saved

    portion_saved = (min_rate + max_rate) // 2

portion_saved /= 10000
print("Best savings rate:", portion_saved)
print("Steps in bisection search:", bisection_count)


