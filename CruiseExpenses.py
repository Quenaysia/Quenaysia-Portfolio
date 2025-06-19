# Name: Quenaysia Hunter
# Program Name: Cruise Expenses
# Description: This program calculates total cruise expenses including excursions and drink charges,
# and determines whether the user stayed within their saving budget.


# Prompt user for savings and initial cruise cost
savings= float (input("Enter your total cruise savings: $"))
initial_expenses= float (input("Enter your initial cruise cost (cruise, airfare, room): $"))

# Accumulator for excursion expenses using a for loop
excursion_total= 0.0
print("\nEnter your 7 excursion expenses:")
for i in range (1, 8):
    cost= float(input(f" Excursion {i} cost: $"))
    excursion_total += cost


# Accumulator for drink expenses using a while loop
drink_total= 0.0
count= 1
print("\nEnter your 12 drink expenses:")
while count <= 12:
        cost = float(input(f" Drink {count} cost: $"))
        drink_total += cost
        count += 1

# Calculate total expenses
total_expenses= initial_expenses + excursion_total + drink_total

# Output results formatted to 2 decimal places
print("\n----- Cruise Expenses Summary -----")
print(f"Initial Cruise Cost: ${initial_expenses: .2f}")
print(f"Total Excursion Cost: ${excursion_total: .2f}")
print(f"Total Drink Cost: ${drink_total: .2f}")
print(f"Overall Total Expenses: ${total_expenses: .2f}")
print(f"Cruise Savings:    ${savings: .2f}")

# Compare expenses to savings
print("\n----- Budget Analysis-----")
if total_expenses <= savings:
    print("You stayed within your budget! No need to find a local job at port.")
else:
    print("You went over your budget! You may need to find a local job at port.")



