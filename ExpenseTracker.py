def menu():
    print("===== EXPENSE TRACKER =====\n"
          "1. Add Expense\n"
          "2. View Expenses\n"
          "3. View Total\n"
          "4. Exit\n")


option = "0"
total = 0
expenses_amount_list = []
expenses_name_list = []
while (option != "4"):
    menu()
    option = input("Select an option:")
    if option == "1":
        expense_name = input("Enter expense name:  ")
        expense_amount = float(input("Enter amount: "))
        print("Expense added!")
        expenses_amount_list.append(expense_amount)
        expenses_name_list.append(expense_name)
    if option == "2":
        for index, names in enumerate(expenses_name_list):
            print(f"{index + 1}. {names}- {expenses_amount_list[index]}\n")
    if option == "3":
        for amount in expenses_amount_list:
            total = total + amount
        print(f"total: {total}")
print("Thanks for using the Expense Tracker!")
