from mini_bank.account import Account
from mini_bank.utils.menu import main_menu, account_menu
from mini_bank.utils.input_utils import get_float, get_nonempty, get_pin
from mini_bank.operations.check_balance import check_balance
from mini_bank.operations.deposit import deposit
from mini_bank.operations.withdraw import withdraw
from mini_bank.operations.transactions import get_transactions
from mini_bank.operations.auth import require_pin
from mini_bank.exceptions import InvalidAmount, InsufficientFunds, AuthenticationError

def main():
    accounts = {}
    while True:
        main_menu()
        c = input("Choose: ").strip()
        if c == "1":
            acc_no = get_nonempty("Enter account number: ")
            if acc_no in accounts:
                print("Account exists")
                continue
            holder = get_nonempty("Holder name: ")
            pin = get_pin("Set PIN: ")
            acc = Account(acc_no, holder)
            acc.set_pin(pin)
            accounts[acc_no] = acc
            print("Account created")
        elif c == "2":
            acc_no = get_nonempty("Enter account number: ")
            acc = accounts.get(acc_no)
            if not acc:
                print("No such account")
                continue
            ok = False
            for _ in range(3):
                pin = get_pin("Enter PIN: ")
                try:
                    require_pin(acc, pin)
                    ok = True
                    break
                except AuthenticationError:
                    print("Invalid PIN")
            if not ok:
                print("Authentication failed")
                continue
            while True:
                account_menu()
                o = input("Choose: ").strip()
                try:
                    if o == "1":
                        print("Balance:", f"{check_balance(acc):.2f}")
                    elif o == "2":
                        amt = get_float("Amount: ")
                        deposit(acc, amt)
                        print("Deposit successful")
                    elif o == "3":
                        amt = get_float("Amount: ")
                        withdraw(acc, amt)
                        print("Withdraw successful")
                    elif o == "4":
                        txs = get_transactions(acc)
                        if not txs:
                            print("No transactions")
                        for t in txs:
                            print(f"{t.timestamp} | {t.type} | {t.amount:.2f}")
                    elif o == "5":
                        break
                    else:
                        print("Invalid option")
                except (InvalidAmount, InsufficientFunds) as e:
                    print("Error:", e)
        elif c == "3":
            if not accounts:
                print("No accounts")
            for a in accounts.values():
                print(a.acc_no, a.holder, f"{a.balance:.2f}")
        elif c == "4":
            print("Exiting")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
