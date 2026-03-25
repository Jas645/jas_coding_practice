import json

budget = []



def load_budget_tracker():
    global budget
    try:
        with open("budget_tracker.json", "r") as f:
            budget = json.load(f)
        print("Budget tracker loaded successfully.")
    except FileNotFoundError:
        budget = []
        
def save_budget_tracker():
    with open("budget_tracker.json", "w") as f:
        json.dump(budget, f)
    print("Budget tracker saved successfully!")

def add_income():
        transaction_amount = float((input("Add new income amount: ")))
        transaction_description = input("Transaction details: ")
        budget.append({'Type': 'income',
                       'Amount': transaction_amount,
                       'Description': transaction_description
                       })
        save_budget_tracker()
        
def add_expense():
        transaction_amount = float((input("Add new expense amount: ")))
        transaction_description = input("Transaction details: ")
        budget.append({'Type': 'expense',
                       'Amount': transaction_amount,
                       'Description': transaction_description
                       })  
        save_budget_tracker()

def show_balance():
    total_income = 0
    total_expenses = 0
    for transaction in budget:
        if transaction["Type"] == 'income':
            total_income += transaction['Amount']
        elif transaction["Type"] == 'expense':
            total_expenses += transaction['Amount']
    balance = total_income - total_expenses  
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Balance: {balance:.2f}")
    
def remove_transaction():
   if not budget:
       print("No Transactions found")
       return
    
   view_transactions()
   try:
        choice = int(input("Which transaction would you like to remove? "))
        index = choice - 1
    
        if 0 <= index < len(budget):
            removed = budget.pop(index)
            print(f"Removed: {removed['Description']} (£{removed['Amount']})")
        else:
            print("Invalid selection. Please try again")
             
   except ValueError:
        print("Please select a valid number.")
        

def view_transactions():
    if not budget:
        print("No Transactions found")
        return
    
    for index, transaction in enumerate(budget, start=1):
        print(f"""{index}. {transaction['Type'].capitalize()}
{transaction['Description']}
£{transaction['Amount']}
""")

def budget_tracker_menu():
    while True:
        print("""
              === Main Menu ===
              1. Add Income
              2. Add Expense
              3. Show Balance
              4. View Transactions
              5. Delete Transaction
              6.Exit
              """)
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            view_transactions()
        elif choice == "5":
            remove_transaction()
        elif choice == '6':
            print('Goodbye!')
            break
        else:
            print('Invalid. Please try again.')



load_budget_tracker()

budget_tracker_menu()

save_budget_tracker()       
              
