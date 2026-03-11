# Bank Management System

A simple command-line based bank management system built with Python.

## Features
- Create new bank accounts
- Deposit money
- Withdraw money
- Check balance
- Transfer money between accounts
- View all accounts
- View transaction history

## Requirements
- Python 3.6 or higher
- No external dependencies required

## Installation

1. Navigate to the project directory:
   cd bank-management-system

2. Run the application:
   python src/main.py

## Usage
1. Run the program
2. Choose options from the menu (1-8)
3. Follow the prompts
4. Exit using option 8

## Example

@"
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.main import Bank, BankAccount

def test_create_account():
    bank = Bank("TestBank")
    acc_num = bank.create_account("Test User", 100)
    assert acc_num == 1001
    assert len(bank.accounts) == 1
    print(" Create account test passed")

def test_deposit():
    account = BankAccount(1001, "Test", 500)
    assert account.deposit(100) == True
    assert account.balance == 600
    assert account.deposit(-50) == False
    print(" Deposit test passed")

def test_withdraw():
    account = BankAccount(1001, "Test", 500)
    assert account.withdraw(200) == True
    assert account.balance == 300
    assert account.withdraw(400) == False
    print(" Withdraw test passed")

def test_transfer():
    bank = Bank("TestBank")
    acc1 = bank.create_account("User1", 1000)
    acc2 = bank.create_account("User2", 500)
    
    assert bank.transfer(acc1, acc2, 300) == True
    assert bank.get_account(acc1).balance == 700
    assert bank.get_account(acc2).balance == 800
    print(" Transfer test passed")

if __name__ == "__main__":
    print("Running tests...\n")
    test_create_account()
    test_deposit()
    test_withdraw()
    test_transfer()
    print("\n All tests passed!")
