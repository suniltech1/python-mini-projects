
# Assignment 2: Smart Wallet with Money Objects
# Wallet stores multiple Money objects and calculates the total amount.

class Money:
    # Constructor to initialize amount and currency
    def __init__(self, amount, currency="Rs"):
        self.amount = amount
        self.currency = currency

    # Human-friendly string representation
    def __str__(self):
        return f"{self.currency} {self.amount}"

    # Developer-friendly representation
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"

    # Overloads the + operator
    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)

    # Overloads the == operator
    def __eq__(self, other):
        return self.amount == other.amount

    # Overloads the < operator (used for sorting)
    def __lt__(self, other):
        return self.amount < other.amount


class Wallet:
    # Stores a list of Money objects
    def __init__(self, notes):
        self.notes = notes

    # Calculates the total value of all notes
    def total(self):
        total_amount = 0

        for note in self.notes:
            total_amount += note.amount

        return Money(total_amount)

    # Allows len(wallet) to work
    def __len__(self):
        return len(self.notes)


# -------------------------
# Test Cases
# -------------------------

a = Money(500)
b = Money(300)

# Test __str__
print(a)

# Test __repr__
print(repr(a))

# Test addition
print(a + b)

# Test equality
print(a == Money(500))

# Test less than
print(b < a)

# Test sorting
notes = [Money(100), Money(500), Money(50)]
print(sorted(notes))

# Test Wallet
w = Wallet(notes)

print(len(w))
print(w.total())