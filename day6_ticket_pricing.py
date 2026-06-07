# Cinema Ticket Pricing System

# Weekday set (for membership + weekday discount check)
weekdays = {"monday", "tuesday", "wednesday", "thursday", "friday"}

# Base full price
base_price = 200  # you can change this if your teacher wants another value

# ---------------- INPUT SECTION ----------------
age = int(input("Enter customer age: "))
day = input("Enter day of the week: ").strip().lower()

member_input = input("Are you a member? (yes/no): ").strip().lower()
is_member = True if member_input == "yes" else False

# ---------------- AGE DISCOUNT ----------------
if age < 5:
    category = "Toddler (Free Entry)"
    price = 0
elif age < 18:
    category = "Minor (50% discount)"
    price = base_price * 0.5
elif age >= 60:
    category = "Senior (30% discount)"
    price = base_price * 0.7
else:
    category = "Adult (Full price)"
    price = base_price

# ---------------- MEMBER + WEEKDAY DISCOUNT ----------------
extra_discount = 0

if is_member and day in weekdays:
    extra_discount = price * 0.10
    price = price - extra_discount

# ---------------- POPCORN OFFER (nested if) ----------------
if is_member:
    if age >= 18:
        popcorn = "Large Popcorn  (Free)"
    else:
        popcorn = "Medium Popcorn  (Free)"
else:
    popcorn = "No free popcorn"

# ---------------- FINAL MESSAGE (ternary expression) ----------------
message = "Free entry " if price == 0 else "Enjoy the show! "

print("\n" + "="*40)
print("        CINEMA TICKET SUMMARY")
print("="*40)

print("Category:", category)
print("Member:", is_member)
print("Day:", day)
print("Extra Discount Applied:", extra_discount)
print("Popcorn Offer:", popcorn)
print("Final Price:", price)
print("Message:", message)
print("="*40)