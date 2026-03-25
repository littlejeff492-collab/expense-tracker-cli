expenses = []

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        item = input("Enter expense item: ")
        amount = float(input("Enter amount: "))
        expenses.append((item, amount))
        print("Expense added!")
    elif choice == "2":
        print("\nExpenses:")
        for item, amount in expenses:
            print(f"{item}: ${amount}")
    elif choice == "3":
        break
    else:
        print("Invalid choice")
