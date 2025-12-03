from mini_bank.exceptions import InvalidAmount

def deposit(account, amount):
    if amount <= 0:
        raise InvalidAmount("Deposit amount must be positive")
    account._balance += amount
    account.add_transaction("deposit", amount)
