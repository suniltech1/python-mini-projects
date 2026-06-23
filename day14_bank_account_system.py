# Bank Account System

# Approach: Used encapsulation with a private balance attribute,for overdraft functionality.
class BankAccount:
    def __init__(self, owner, opening_amount=0):
        self.owner = owner
        self.__balance = 0

        if opening_amount >= 0:
            self.__balance = opening_amount
        else:
            print("Opening balance cannot be negative!")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return

        self.__balance += amount
        print(f"Deposited Rs {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return

        if amount > self.__balance:
            print("Not enough balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn Rs {amount}")

    def get_balance(self):
        return self.__balance

    # Helper method for child classes
    def _update_balance(self, amount):
        self.__balance += amount


class SavingsAccount(BankAccount):
    def __init__(self, owner, opening_amount=0):
        super().__init__(owner, opening_amount)

    def add_interest(self, rate):
        if rate < 0:
            print("Interest rate cannot be negative!")
            return

        interest = self.get_balance() * rate / 100
        self._update_balance(interest)
        print(f"Interest added: Rs {interest}")


class CurrentAccount(BankAccount):
    def __init__(self, owner, opening_amount=0, overdraft_limit=0):
        super().__init__(owner, opening_amount)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return

        new_balance = self.get_balance() - amount

        if new_balance < -self.overdraft_limit:
            print("Overdraft limit reached!")
        else:
            self._update_balance(-amount)
            print(f"Withdrawn Rs {amount}")



# Testing


print("=== Savings Account ===")
s = SavingsAccount("Asha", 1000)

s.deposit(500)
s.add_interest(10)
print("Balance:", s.get_balance())

s.withdraw(5000)

print("\n=== Current Account ===")
c = CurrentAccount("Bibek", 200, overdraft_limit=500)

c.withdraw(600)
print("Balance:", c.get_balance())

c.withdraw(200)

print("\n=== Validation Tests ===")
s.deposit(-100)
s.withdraw(-50)