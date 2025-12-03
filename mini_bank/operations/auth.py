from mini_bank.exceptions import AuthenticationError

def require_pin(account, pin):
    if not account.verify_pin(pin):
        raise AuthenticationError("Invalid PIN")
