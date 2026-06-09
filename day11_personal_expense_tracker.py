# Task 1: Load expenses from file
def load_expenses(filename):
    expenses = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    category, amount = line.split(",")
                    expenses.append((category, float(amount)))
    except FileNotFoundError:
        return []

    return expenses


# Task 2: Add a new expense
def add_expense(filename, category, amount):
    if amount < 0:
        raise ValueError("Amount must be a positive number.")

    with open(filename, "a") as file:
        file.write(f"{category},{amount}\n")


# Task 3: Calculate totals by category
def category_totals(expenses):
    totals = {}

    for category, amount in expenses:
        totals[category] = totals.get(category, 0) + amount

    print("Category         Total")
    print("───────────────────────")

    grand_total = 0

    for category, total in totals.items():
        print(f"{category:<15}: ${total:.2f}")
        grand_total += total

    print("───────────────────────")
    print(f"{'Grand Total':<15}: ${grand_total:.2f}")


# Task 4: Expenses above a threshold
def above_threshold(expenses, limit):
    return [(c, a) for c, a in expenses if a > limit]


# Main Program

filename = "expenses.txt"

# Load expenses
expenses = load_expenses(filename)

# Display category totals
category_totals(expenses)

# Show expenses above $100
limit = 100
high_expenses = above_threshold(expenses, limit)

print(f"\nExpenses above ${limit}:")
for category, amount in high_expenses:
    print(f"  {category:<14} → ${amount:.2f}")
