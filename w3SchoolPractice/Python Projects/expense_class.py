import csv
import datetime

# Predefined list of expense types
expense_types = ["Food", "Rent", "Shopping", "Utilities", "Other"]
csv_file = 'Expense_csv.csv'

class Expense:
    def __init__(self, expense_name, amount, expense_type, mode_of_transaction):
        self.expense_name = expense_name
        self.amount = amount
        self.expense_type = expense_type
        self.mode_of_transaction = mode_of_transaction
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"{self.expense_name} | {self.amount} | {self.expense_type} | {self.mode_of_transaction} | {self.date}"

    def save_to_csv(self, file_name):
        try:
            with open(file_name, mode='x', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Expense Name", "Amount", "Expense Type", "Mode of Transaction", "Date"])
                writer.writerow([self.expense_name, self.amount, self.expense_type, self.mode_of_transaction, self.date])
        except FileExistsError:
            with open(file_name, mode='a', newline="") as file:
                writer = csv.writer(file)
                writer.writerow([self.expense_name, self.amount, self.expense_type, self.mode_of_transaction, self.date])

    @staticmethod
    def add_expense():
        try:
            expense_name = input("Enter the name of the expense: ").strip()
            print("-" * 100)
            amount = int(input("Enter the amount: "))
            print("-" * 100)
            print("Select the type of expense from the following:")
            for i, typ in enumerate(expense_types, start=1):
                print(f"{i}. {typ}")
            expense_type_index = int(input("Enter the number corresponding to the expense type: ")) - 1
            if not (0 <= expense_type_index < len(expense_types)):
                raise ValueError("Invalid expense type selected.")
            expense_type = expense_types[expense_type_index]
            mode_of_transaction = input("Enter the mode of transaction (Cash or Online): ").strip()
            print("-" * 100)

            new_expense = Expense(expense_name, amount, expense_type, mode_of_transaction)
            new_expense.save_to_csv(csv_file)
            print("✅ Expense added successfully!")
        except ValueError as ve:
            print(f"⚠️ Error: {ve}")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")

    @staticmethod
    def fetch_expense():
        try:
            total_expense = 0
            expense_breakdown = {}
            with open(csv_file, mode='r', newline="") as file:
                reader = csv.reader(file)
                header = next(reader)
                print("-" * 100)
                print(f"{' | '.join(header)}")
                print("-" * 100)

                for row in reader:
                    total_expense += int(row[1])
                    expense_type = row[2]
                    expense_breakdown[expense_type] = expense_breakdown.get(expense_type, 0) + int(row[1])
                    print(f"Expense Name: {row[0]}, Amount: {row[1]}, Type: {row[2]}, Mode: {row[3]}, Date: {row[4]}")
                    print("-" * 100)

            print(f"💰 Total Expense: {total_expense}")
            print("-" * 100)
            print("📊 Expense Breakdown by Type:")
            for exp_type, total in expense_breakdown.items():
                print(f"{exp_type}: {total}")
            print("-" * 100)
        except FileNotFoundError:
            print("⚠️ CSV file not found. Please add some expenses first.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")

    @staticmethod
    def fetch_expense_period():
        try:
            year = input("Enter the year (e.g., 2025): ").strip()
            month = input("Enter the month (e.g., January: 01): ").strip()
            total_expense = 0
            expense_breakdown = {}

            with open(csv_file, mode='r', newline="") as file:
                reader = csv.reader(file)
                header = next(reader)
                print("-" * 100)
                print(f"{' | '.join(header)}")
                print("-" * 100)

                for row in reader:
                    if row[4][:7] == f"{year}-{month}":
                        total_expense += int(row[1])
                        expense_type = row[2]
                        expense_breakdown[expense_type] = expense_breakdown.get(expense_type, 0) + int(row[1])
                        print(f"Expense Name: {row[0]}, Amount: {row[1]}, Type: {row[2]}, Mode: {row[3]}, Date: {row[4]}")
                        print("-" * 100)

            print(f"💰 Total Expense for {year}-{month}: {total_expense}")
            print("-" * 100)
            print("📊 Expense Breakdown by Type:")
            for exp_type, total in expense_breakdown.items():
                print(f"{exp_type}: {total}")
            print("-" * 100)
        except FileNotFoundError:
            print("⚠️ CSV file not found. Please add some expenses first.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")

# Example usage
# Uncomment the lines below to test the functionality
# Expense.add_expense()
# Expense.fetch_expense()
# Expense.fetch_expense_period()
