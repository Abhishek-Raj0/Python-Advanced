class BankAccount:
    def __init__(self, owner, balance = 0):
        self.balance = balance
        self.owner = owner
    # Implement deposit, withdraw

    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

account = BankAccount("Alice")
import sys
for line in sys.stdin:
    parts = line.strip().split()
    if not parts:
        continue
    cmd = parts[0]
    # Handle the three commands

    if cmd == "deposit":
        amount = int(parts[1])
        account.deposit(amount)

    elif cmd == "withdraw":
        amount = int(parts[1])
        try:
            account.withdraw(amount)
        except ValueError as e:
            print(f"{e}")

    elif cmd == "balance":
        print(account.balance)

    else:
        print(f"Unknown command: {cmd}")