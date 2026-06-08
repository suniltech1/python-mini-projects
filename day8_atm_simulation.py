# ATM Simulation System

# Account Information
account = {
    "name": "sunil khadka",
    "account_number": "123456789",
    "pin": 1234,
    "balance": 1000.0
}

# Transaction History
transactions = []

# PIN Verification
entered_pin = int(input("Enter your PIN: "))

if entered_pin != account["pin"]:
    print("Invalid PIN! Access Denied.")
else:
    print(f"\nWelcome, {account['name']}!")

    while True:
        print("\n===== Choose options =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Account Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        # Check Balance
        if choice == "1":
            print(f"Current Balance: Rs.{account['balance']:.2f}")

        # Deposit Money
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                account["balance"] += amount
                transactions.append(f"Deposited Rs.{amount:.2f}")
                print("Deposit successful!")
                print (f"New Balance: Rs.{account['balance']:.2f}")
            else:
                print("Invalid amount!")

        # Withdraw Money
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount!")
            elif amount > account["balance"]:
                print("Insufficient balance!")
            else:
                account["balance"] -= amount
                transactions.append(f"Withdrew Rs.{amount:.2f}")
                print("Withdrawal successful!")
                print(f"New Balance: Rs.{account['balance']:.2f}")

        # Transaction History
        elif choice == "4":
            print("\n===== TRANSACTION HISTORY =====")

            if len(transactions) == 0:
                print("No transactions yet.")
            else:
                for transaction in transactions:
                    print(transaction)

        # Account Details 
        elif choice == "5":
            print("\n===== ACCOUNT SUMMARY =====")
            print("Name:", account["name"])
            print("Account Number:", account["account_number"])
            print("Current Balance:", account["balance"])
            print("Account Holder's Name:", account["name"][0].upper() + account["name"][1:])
            print("Total Transactions:", len(transactions))


        # Exit
        elif choice == "6":
            print("\nThank you for using our ATM!")

            break;

        else:
            print("Invalid choice! Please try again.")