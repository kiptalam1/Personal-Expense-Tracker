from datetime import datetime
import json
import pandas as pd


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

expenses = load_expenses()

def add_expense():
    category = input('Enter Category: ').strip()
    amount = float(input('Enter the amount: '))
    date = input('Enter the date (YYYY-MM-DD) or press enter for today: ').strip()
    # enter today's date if not provided.
    date = date if date else datetime.today().strftime("%Y-%m-%d")
    
    if category:    
        expenses.append({'category': category, 'amount': amount, 'date': date})
        save_expenses(expenses)
        print("Expenses added successfully.")
    else:
        return
    

def view_expenses(expenses):
    if not expenses:
        print("No expenses to display.")
        return
    else:
        df = pd.DataFrame(DATA_FILE)
        print("\nExpenses:")
        return df
    
    
    
add_expense()
print(view_expenses())





# if __name__ == '__main__':
#     main()