import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILENAME = "expenses_graph.csv"

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, Shopping etc): ")
    note = input("Enter note: ")
    date = input("Enter date (YYYY-MM-DD): ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, note, date])

    print("Expense added successfully!\n")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found.")
        return

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        print("\nAmount | Category | Note | Date")
        print("-"*40)
        for row in reader:
            print(" | ".join(row))

def monthly_report():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    if not os.path.exists(FILENAME):
        print("No expenses found.")
        return

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3].startswith(month):
                total += float(row[0])

    print(f"Total spent in {month} = ₹{total}")

def show_graph():
    if not os.path.exists(FILENAME):
        print("No expenses found.")
        return

    data = {}

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            category = row[1]
            amount = float(row[0])
            data[category] = data.get(category, 0) + amount

    plt.bar(data.keys(), data.values())
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

while True:
    print("\n=== Visual Expense Analyzer ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Report")
    print("4. Show Spending Graph")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        monthly_report()
    elif choice == "4":
        show_graph()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
