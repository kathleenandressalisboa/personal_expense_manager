import report

expenses = []

def add_expense():
    description = input('Description: ')

    try:
        amount = float(input('Amount: '))
    except ValueError:
        print('Invalid amount!\n')
        return

    category = input('Category: ').lower()

    expense = {
        "description": description,
        "amount": amount,
        "category": category,
    }

    expenses.append(expense)
    print("expense added successfully!\n")

def list_expenses():
    if not expenses:
        print('No expenses recorded.\n')
        return

    for i, expense in enumerate(expenses, start = 1):
        print(f"{i}. {expense['description']} - ${expense['amount']:.2f} - {expense['category']}")
    print()

def get_expense():
    return expenses

def menu():
    while True:
        print("==== ESPENSE TRACKER ====")
        print("1 - Add expense")
        print("2 - List expenses")
        print("3 - Show total spent")
        print("4 - Show total by category")
        print("5 - Exit")

        option = input("Choose on option: ")

        if option == "1":
            add_expense()
        elif option == "2":
            list_expenses()
        elif option == "3":
            report.show_total(get_expense())
        elif option == "4":
            report.total_by_category(get_expense())
        elif option == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid option!\n")

if __name__ == "__main__":
    menu()

