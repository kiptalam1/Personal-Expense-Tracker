from datetime import datetime
import json
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = 'expenses.json'

def load_expenses():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    category = input('Enter Category: ').strip()
    amount = float(input('Enter the amount: '))
    date = input('Enter the date (YYYY-MM-DD) or press enter for today: ').strip()
    # enter today's date if not provided.
    date = date if date else datetime.today().strftime("%Y-%m-%d")
    
    if category:    
        expenses.append({'category': category, 'amount': amount, 'date': date})
        save_expenses(expenses)
        print("Expense added successfully.")
    else:
        return

def view_expenses(expenses):
    if not expenses:
        print("No expenses to display.")
        return
    df = pd.DataFrame(expenses)
    print("\nExpenses:")
    print(df)
        
def analyze_expenses(expenses):
    if not expenses:
        print("There are no expenses to analyse.")
        return
    df = pd.DataFrame(expenses)
    df['amount'] = df['amount'].astype(float)
    
    total = df['amount'].sum()
    print(f"\nTotal Expenses: {total:.2f}")
    
    category_totals = df.groupby('category')['amount'].sum()
    print(f"\nSpending by category")
    print(category_totals)
    
    #plot the spending as a pie chart
    plt.figure(figsize=(6,6))
    category_totals.plot(kind='pie', autopct="%1.1f%%", startangle=140)
    plt.title("Spending by Category")
    plt.ylabel("")
    plt.show()
    
def main():
    expenses = load_expenses()
    while True:
        print("Personal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            analyze_expenses(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()