def show_total(expenses):
    if not expenses:
        print("No expenses recorded.\n")
        return

    total = sum(expense ["amont"] for expense in expenses)
    print(f"Total spent: &{total:.2f}\n")

def total_by_category(expenses):
    if not expenses:
        print("No expenses recorded.\n")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("Expenses by category:")
    for category, total in categories.items():
        print(f"{category}: ${total:.2f}")
    print()