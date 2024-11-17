from transactions import TransactionManager
from financials import FinancialManager

def main_menu():
    transaction_manager = TransactionManager()

    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Show Summary of Transactions")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter the amount: "))
            description = input("Enter a description: ")
            print(transaction_manager.add_transaction(amount, description, 'income'))
        elif choice == '2':
            amount = float(input("Enter the amount: "))
            description = input("Enter a description: ")
            print(transaction_manager.add_transaction(amount, description, 'expense'))
        elif choice == '3':
            financial_manager = FinancialManager(transaction_manager.get_transactions())
            print(f"Current Balance: {financial_manager.calculate_balance()}")
        elif choice == '4':
            financial_manager = FinancialManager(transaction_manager.get_transactions())
            print("Transaction Summary:")
            for line in financial_manager.generate_summary():
                print(line)
        elif choice == '5':
            print("Thank you for using the Personal Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main_menu()
