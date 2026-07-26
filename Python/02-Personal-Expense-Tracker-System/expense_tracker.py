import csv
import os

FILE_NAME = "expenses.csv"

# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])

# 1. Add Expense
def add_expense():
    try:
        date = input("Enter Date (DD-MM-YYYY): ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount])

        print("\nExpense added successfully!\n")

    except ValueError:
        print("Invalid amount! Please enter a numeric value.\n")

    except Exception as e:
        print("Error:", e)


# 2. View Expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            next(reader)  # Skip header

            print("\n----- Expense Records -----")
            print("Date\t\tCategory\tAmount")

            rows = list(reader)

            if len(rows) == 0:
                print("No expenses found.")

            else:
                for row in rows:
                    print(f"{row[0]}\t{row[1]}\t\t{row[2]}")

            print()

    except FileNotFoundError:
        print("File not found.")

    except Exception as e:
        print("Error:", e)


# 3. Total Expense
def total_expense():
    total = 0

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            next(reader)  # Skip header

            for row in reader:
                total += float(row[2])

        print(f"\nTotal Expense = {total}\n")

    except FileNotFoundError:
        print("File not found.")

    except Exception as e:
        print("Error:", e)


# 4. Search by Category
def search_category():
    category = input("Enter Category to Search: ").lower()

    found = False

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            next(reader)  # Skip header

            print("\n----- Matching Expenses -----")
            print("Date\t\tCategory\tAmount")

            for row in reader:
                if row[1].lower() == category:
                    found = True
                    print(f"{row[0]}\t{row[1]}\t\t{row[2]}")

            if not found:
                print("No matching category found.")

            print()

    except FileNotFoundError:
        print("File not found.")

    except Exception as e:
        print("Error:", e)


# Main Menu
def menu():
    while True:
        print("========== Personal Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Search by Category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            search_category()

        elif choice == "5":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please try again.\n")


# Program Starts Here
create_file()
menu()