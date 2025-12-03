Mini Bank Application 🏦🐍

A Python-based console application that allows users to perform basic banking operations such as creating accounts, secure authentication, deposits, withdrawals, and viewing transaction history.
This project demonstrates core Python concepts including OOP, modular coding, custom exceptions, hashing, and input validation.

Features

✔️ Create new bank accounts
✔️ Secure PIN authentication (SHA-256 hashing)
✔️ Check account balance
✔️ Deposit money
✔️ Withdraw money safely
✔️ View complete transaction history
✔️ In-memory data storage (no database)
✔️ Clean modular project structure

Technologies Used
Backend:

Python (Core Python)

Dataclasses

hashlib (SHA-256)

getpass

Project Structure:

Modular Python packages

Separate operation files

Custom exception handling

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

How to Run

Install Python and run:

python -m mini_bank.main


To use a batch file:

python -m mini_bank.main
pause

Notes

All data is temporary (in-memory only).

No database is used.

PINs are hashed using SHA-256 for security.

Ideal for learning Core Python fundamentals.

Done by: Kiran Poojary
