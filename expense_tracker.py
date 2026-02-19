expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expenses.append({"amount": amount, "category": category})
    print("Expense added successfully!\n")

def view_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Expenses: ₹{total}\n")

def view_by_category():
    categories = {}
    for expense in expenses:
        if expense["category"] in categories:
            categories[expense["category"]] += expense["amount"]
        else:
            categories[expense["category"]] = expense["amount"]
    
    print("Expenses by Category:")
    for category, amount in categories.items():
        print(f"{category}: ₹{amount}")
    print()

def main():
    while True:
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_total()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
