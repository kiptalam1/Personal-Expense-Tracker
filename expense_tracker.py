from datetime import datetime

expenses = []
def add_expense():
    category = input('Enter Category: ').strip()
    amount = float(input('Enter the amount: '))
    date = input('Enter the date (YYYY-MM-DD) or press enter for today: ').strip()
    
    # enter today's date if not provided.
    date = date if date else datetime.today().strftime("%Y-%m-%d")
    
    expenses.append({'category': category, 'amount': amount, 'date': date})
        
    print("Expenses added successfully.")
    
add_expense()
print(expenses)
# if __name__ == '__main__':
#     main()
