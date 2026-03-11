#!/usr/bin/env python3
"""
Bank Management System - Main Application
"""

class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ")
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ")
            return True
        return False
    
    def check_balance(self):
        return self.balance
    
    def get_transactions(self):
        return self.transactions
    
    def __str__(self):
        return f"Account {self.account_number}: {self.name} - Balance: "

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.next_account_number = 1001
    
    def create_account(self, name, initial_deposit=0):
        account_number = self.next_account_number
        self.next_account_number += 1
        
        account = BankAccount(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        return account_number
    
    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
    def transfer(self, from_acc, to_acc, amount):
        from_account = self.get_account(from_acc)
        to_account = self.get_account(to_acc)
        
        if from_account and to_account and from_account.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False
    
    def list_accounts(self):
        for account in self.accounts.values():
            print(account)

def main():
    # Create a new bank
    bank = Bank("MyBank")
    
    while True:
        print("\n" + "="*40)
        print("     BANK MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. View All Accounts")
        print("7. View Transaction History")
        print("8. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            name = input("Enter customer name: ")
            try:
                initial = float(input("Enter initial deposit (0 if none): "))
                acc_num = bank.create_account(name, initial)
                print(f"Account created successfully! Account Number: {acc_num}")
            except ValueError:
                print("Invalid amount! Please enter a number.")
        
        elif choice == '2':
            try:
                acc_num = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))
                account = bank.get_account(acc_num)
                if account and account.deposit(amount):
                    print(f"Deposit successful! New balance: ")
                else:
                    print("Deposit failed!")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        
        elif choice == '3':
            try:
                acc_num = int(input("Enter account number: "))
                amount = float(input("Enter withdrawal amount: "))
                account = bank.get_account(acc_num)
                if account and account.withdraw(amount):
                    print(f"Withdrawal successful! New balance: ")
                else:
                    print("Withdrawal failed! Insufficient funds.")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        
        elif choice == '4':
            try:
                acc_num = int(input("Enter account number: "))
                account = bank.get_account(acc_num)
                if account:
                    print(f"Current balance: ")
                else:
                    print("Account not found!")
            except ValueError:
                print("Invalid account number!")
        
        elif choice == '5':
            try:
                from_acc = int(input("Enter source account number: "))
                to_acc = int(input("Enter destination account number: "))
                amount = float(input("Enter transfer amount: "))
                if bank.transfer(from_acc, to_acc, amount):
                    print("Transfer successful!")
                else:
                    print("Transfer failed!")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        
        elif choice == '6':
            print("\nAll Accounts:")
            if bank.accounts:
                bank.list_accounts()
            else:
                print("No accounts found.")
        
        elif choice == '7':
            try:
                acc_num = int(input("Enter account number: "))
                account = bank.get_account(acc_num)
                if account:
                    print("\nTransaction History:")
                    transactions = account.get_transactions()
                    if transactions:
                        for transaction in transactions:
                            print(f"   {transaction}")
                    else:
                        print("  No transactions yet.")
                else:
                    print("Account not found!")
            except ValueError:
                print("Invalid account number!")
        
        elif choice == '8':
            print("Thank you for using Bank Management System!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
