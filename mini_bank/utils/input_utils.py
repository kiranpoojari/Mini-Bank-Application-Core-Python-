import getpass

def get_float(prompt):
    while True:
        v = input(prompt).strip()
        try:
            return float(v)
        except ValueError:
            print("Invalid number, try again")

def get_nonempty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Input cannot be empty")

def get_pin(prompt):
    while True:
        p = getpass.getpass(prompt)
        if p:
            return p
        print("PIN cannot be empty")
