class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0 
    def __init__(self, balance: int, name: str) -> None:
        self.balance = balance
        self.name = name
        BankAccount.total_balance += balance
        BankAccount.total_accounts+= 1


# TODO: Create two accounts
Alice = BankAccount(1000, "Alice")
Bob = BankAccount(2000, "Bob")
# TODO: Print the information using the mentioned format

print(f"Alice's balance: ${Alice.balance}")
print(f"Bob's balance: ${Bob.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")