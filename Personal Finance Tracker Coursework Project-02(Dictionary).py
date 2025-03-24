#Import JSON module
import json
#Import datetime module
from datetime import datetime

#Global dictionary to store transactions
transactions = {}

#File path for JSON data
file_path = "transactions.json"

#File handling functions

#This function used to load transactions from a json file
def load_transactions(file_path):
    global transactions
    #Open the JSON file in read mode
    try:
        with open(file_path, "r") as file:
            data = file.read()
            if data:
                #Load the desrialized JSON data into the transactions list
                transactions = json.loads(data)
            else:
                transactions = {}
    except FileNotFoundError:
        print("Transactions file not found. Creating new transactions dictionary.")
        transactions = {}
    except json.JSONDecodeError:
        print("Error!JSON data in the file is not in a correct format")

#This function used to save transactions to a json file
def save_transactions():
    #Open the JSON file in write mode
     try:
        with open(file_path, "w") as file:
            #Write the serialized contents of the transaction list to the file
            json.dump(transactions, file, indent=4)
        print("Transactions saved successfully.")
     except Exception as e:
        print("Error occurred while saving transactions:", e)

#This function used to read bulk transactions from a file and transactions dictionary  
def read_bulk_transactions_from_file(filename):
    try:
        with open(filename, "r") as file:
            bulk_data = json.load(file)
            for key, value in bulk_data.items():
                print(f"Read the File: Key:{key}, Value:{value}")                  
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON data from file.")
    except Exception as e:
        print("An error occurred:", e)

#Feature implementations

#This function used to add a transaction to the transactions dictionary        
def add_transaction():
    try:
        transaction_type = input("Enter transaction type as Salary or Groceries: ").capitalize()
        if transaction_type != "Salary" and transaction_type != "Groceries":
            raise Exception("Invalid transaction_type") 
        amount = float(input("Enter transaction amount: "))
        date_str = input("Enter transaction date (YYYY-MM-DD): ")
        
        # Validate date format
        date = datetime.strptime(date_str, "%Y-%m-%d")
        
        transaction = {"amount": amount, "date": date.strftime("%Y-%m-%d")}
        
        if transaction_type in transactions:
            transactions[transaction_type].append(transaction)
        else:
            transactions[transaction_type] = [transaction]
        
        print("Transaction added successfully.")
        save_transactions() 
    except ValueError:
        print("Invalid input. Please enter a valid number for amount or date in format YYYY-MM-DD.")
    except Exception as e:
        print("An error occurred:", e)

#This function used to view all transactions in the transactions dictionary
def view_transactions():
    try:
        for transaction_type, transactions_list in transactions.items():
            print(f"{transaction_type}:")
            for transaction in transactions_list:
                print(f"Amount: {transaction['amount']}, Date: {transaction['date']}")
            print()
    except Exception as e:
        print("An error occurred:", e)

#This function used to update transaction in the transactions dictionary
def update_transaction():
    try:
        transaction_type = input("Enter transaction type to update: ").capitalize()
        if transaction_type in transactions:
            print("Transactions for", transaction_type)
            for index, transaction in enumerate(transactions[transaction_type]):
                print(index, "Amount:", transaction['amount'], "Date:", transaction['date'])
            index = int(input("Enter index to update: "))
            amount = float(input("Enter updated amount: "))
            date_str = input("Enter updated date (YYYY-MM-DD): ")
            
            #Validate date format
            date = datetime.strptime(date_str, "%Y-%m-%d")
            
            transactions[transaction_type][index] = {"amount": amount, "date": date.strftime("%Y-%m-%d")}
            print("Transaction updated successfully.")
            save_transactions() 
        else:
            print("No transactions found for", transaction_type)
    except (IndexError, ValueError):
        print("Invalid input or index out of range.")

#This function used to delete transaction in the transactions dictionary
def delete_transaction():
    try:
        transaction_type = input("Enter transaction type to delete: ").capitalize()
        if transaction_type in transactions:
            print("Transactions for", transaction_type)
            for index, transaction in enumerate(transactions[transaction_type]):
                print(index, "Amount:", transaction['amount'], "Date:", transaction['date'])
            index = int(input("Enter index to delete: "))
            del transactions[transaction_type][index]
            print("Transaction deleted successfully.")
            save_transactions()
        else:
            print("No transactions found for", transaction_type)
    except (IndexError, ValueError):
        print("Invalid input or index out of range.")

#This function used to display summary of transactions
def display_summary():
    try:
        for transaction_type, transactions_list in transactions.items():
            total_amount = sum(transaction['amount'] for transaction in transactions_list)
            #for each transaction type and get the total amount of that has been made
            print(f"{transaction_type}: Total Amount = {total_amount}")
    except Exception as e:
        print("An error occurred:", e)

#Main menu function handle user interactions
def main_menu():
    #load the existing transactions data from the JSON file
    load_transactions("transactions.json")    
    #Main loop program(Main_menu)
    while True:
        try:
            print("\n===== Personal Finance Tracker =====")
            print("1. Add Transaction")
            print("2. View Transactions")
            print("3. Update Transaction")
            print("4. Delete Transaction")
            print("5. Display Summary")
            print("6. Read Bulk Transactions from File")
            print("7. Exit\n")
            choice = input("Enter your choice: ")

            if choice == "1":
                add_transaction()
            elif choice == "2":
                view_transactions()
            elif choice == "3":
                update_transaction()
            elif choice == "4":
                delete_transaction()
            elif choice == "5":
                display_summary()
            elif choice == "6":
                filename = input("Enter filename to read bulk transactions from: ")
                read_bulk_transactions_from_file(filename)
            elif choice == "7":
                save_transactions()#Save transactions before exiting from the personal finance tracker
                print("Good Bye!Exiting From the Personal Finance Tracker")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("An unexpected error occurred:", e)

#Start the program           
if __name__ == "__main__":
    main_menu()

#if you are paid to do this assignment please delete this line of comment.
