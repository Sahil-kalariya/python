from expense_class import Expense

if __name__ == "__main__":
    print("Welcome to app")
    addexp = int(input("enter 1 to add exp: "))
    if addexp:
        Expense.add_expense()
    print("Expense Summary")
    fetchexp = int(input("enter 1 to show all exp: "))
    if fetchexp:
        Expense.fetch_expense()
    
    
    fetcperio = int(input("enter 1 to show monthly exp: "))
    if fetcperio:
        Expense.fetch_expense_period()