Mini Bank Application (Core Python)

This is a simple console-based banking application built using Core Python.
It demonstrates object-oriented programming, modular code structure, input validation, and PIN-based security — all without using any database.

Features

Create account

Secure PIN authentication

Check balance

Deposit money

Withdraw money

View transaction history

Handles invalid inputs safely

Fully in-memory (no database required)

Project Structure
mini_bank/
├── account.py
├── exceptions.py
├── main.py
│
├── operations/
│   ├── check_balance.py
│   ├── deposit.py
│   ├── withdraw.py
│   ├── transactions.py
│   └── auth.py
│
└── utils/
    ├── input_utils.py
    └── menu.py

Concepts Used

Classes and Objects

Encapsulation

Custom Exceptions

Modular Code Organization

SHA-256 Hashing for PIN

Menu-Driven Program

Input Validation

How to Run

Run the application using:

python -m mini_bank.main


Optional run.bat file:

python -m mini_bank.main
pause


Double-click run.bat to launch the app.

Example Output
=== MINI BANK ===
1. Create account
2. Select account
3. List accounts
4. Exit

Future Improvements

Add data storage using JSON or SQLite

Add PIN change feature

Add mini-statement options

Add admin role

Author

Kiran Poojary
