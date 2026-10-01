expenses = []  # each entry = one day's expense


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def show_menu():
    print("=" * 25)
    print("Your Expense Tracker")
    print("=" * 25)
    print("0. Enter today's expense")
    print("1. Daily expense")
    print("2. Weekly expense (last 7 days)")
    print("3. Monthly expense (last 30 days)")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Select your choice: ").strip()

    if choice == "0":
        amount = get_number("Enter your expense: ")
        expenses.append(amount)
        print("You have added expense successfully")

    elif choice == "1":
        if expenses:
            print(f"Your daily expense is: {expenses[-1]}")
        else:
            print("No expenses added yet.")

    elif choice == "2":
        weekly = sum(expenses[-7:])
        print(f"Your weekly expense is: {weekly}")

    elif choice == "3":
        monthly = sum(expenses[-30:])
        print(f"Your monthly expense is: {monthly}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")