# ==========================================
# DecodeLabs Internship - Project 2
# Expense Tracker
# ==========================================

expenses = []
total = 0.0


def add_expense():
    global total

    print("\n--- Add Expense ---")

    amount = input("Enter expense amount: ").strip()

    try:
        amount = float(amount)

        if amount <= 0:
            print("Expense amount must be greater than 0.")
            return

        expenses.append(amount)

        # Accumulator pattern
        total += amount

        print(f"Expense of ${amount:.2f} added successfully.")
        print(f"Current Total: ${total:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


def view_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded.")
        return

    for index, amount in enumerate(expenses, start=1):
        print(f"{index}. ${amount:.2f}")


def view_total():
    print("\n--- Total Spent ---")
    print(f"Total Spent: ${total:.2f}")


def view_summary():
    print("\n========== EXPENSE SUMMARY ==========")

    if not expenses:
        print("No expenses recorded.")
        print("=====================================")
        return

    average = total / len(expenses)

    print(f"Number of Expenses : {len(expenses)}")
    print(f"Total Spent        : ${total:.2f}")
    print(f"Average Expense    : ${average:.2f}")
    print(f"Highest Expense    : ${max(expenses):.2f}")
    print(f"Lowest Expense     : ${min(expenses):.2f}")

    print("=====================================")


def main():
    while True:

        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. View Expense Summary")
        print("5. Exit")
        print("=====================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            view_total()

        elif choice == "4":
            view_summary()

        elif choice == "5":
            print("\n========== FINAL SUMMARY ==========")
            print(f"Total Expenses: {len(expenses)}")
            print(f"Final Total Spent: ${total:.2f}")
            print("===================================")
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()
