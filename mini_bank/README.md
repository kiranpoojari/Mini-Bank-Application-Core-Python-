Mini Bank Application (Core Python)

A simple console-based banking application built using Core Python.
It demonstrates clean modular design, OOP concepts, input validation, and PIN-based security — all running fully in-memory without any database.

📌 Features

Create new bank accounts

Secure PIN authentication (SHA-256 hashed)

Check account balance

Deposit money

Withdraw money

View full transaction history

Safe handling of invalid inputs

Lightweight & fast — no external database

📂 Project Structure
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

🧠 Concepts Used

Classes & Objects

Encapsulation

Custom Exceptions

Modular Code Architecture

SHA-256 Hashing for PIN security

Menu-driven flow

Input validation techniques

▶️ How to Run
Run using Python module:
python -m mini_bank.main

Optional (run.bat):
python -m mini_bank.main
pause


Double-click run.bat to launch the application instantly.

💻 Example Output
=== MINI BANK ===
1. Create account
2. Select account
3. List accounts
4. Exit

🚀 Future Improvements

Add persistent storage (JSON / SQLite)

Add PIN change option

Add mini-statement feature

Add admin role for managing accounts

👤 Author

Kiran Poojary
