from datetime import datetime
import json

DATA_FILE = 'expenses.json'

def load_expenses():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

expenses = []

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    category = input('Enter Category: ').strip()
    amount = float(input('Enter the amount: '))
    date = input('Enter the date (YYYY-MM-DD) or press enter for today: ').strip()
    
    # enter today's date if not provided.
    date = date if date else datetime.today().strftime("%Y-%m-%d")
    
    expenses.append({'category': category, 'amount': amount, 'date': date})
        
    print("Expenses added successfully.")
    
load_expenses()
print(expenses)






# if __name__ == '__main__':
#     main()
