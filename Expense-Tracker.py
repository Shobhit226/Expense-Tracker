import csv
from datetime import datetime
from collections import defaultdict

FILENAME = "expenses.csv"

def add_expense(filename):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport): ")
    amount = input("Enter amount: ")
    note = input("Enter note (optional): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
        amount = float(amount)
    except ValueError:
        print("Invalid date or amount format.")
        return

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
        print("✅ Expense added successfully!")

def view_expenses(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            print("\n--- All Expenses ---\n")
            for row in reader:
                print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Note: {row[3]}")
    except FileNotFoundError:
        print("⚠️ No expenses found. File does not exist yet.")

def view_summary(filename):
    summary = defaultdict(float)
    total = 0.0
    month = input("Enter month to summarize (YYYY-MM): ")

    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].startswith(month):
                    summary[row[1]] += float(row[2])
                    total += float(row[2])
    except FileNotFoundError:
        print("⚠️ Expense file not found.")
        return

    print(f"\n--- Summary for {month} ---\n")
    for category, amount in summary.items():
        print(f"{category}: {amount:.2f}")
    print(f"Total Spent: {total:.2f}")

def main():
    while True:
        print("\n==== Personal Expense Tracker ====\n")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Monthly Summary")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense(FILENAME)
        elif choice == '2':
            view_expenses(FILENAME)
        elif choice == '3':
            view_summary(FILENAME)
        elif choice == '4':
            print("👋 Exiting... Stay financially wise!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()