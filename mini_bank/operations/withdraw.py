from mini_bank.exceptions import InvalidAmount, InsufficientFunds

def withdraw(account, amount):
    if amount <= 0:
        raise InvalidAmount("Withdraw amount must be positive")
    if amount > account.balance:
        raise InsufficientFunds("Insufficient balance")
    account._balance -= amount
    account.add_transaction("withdraw", amount)
