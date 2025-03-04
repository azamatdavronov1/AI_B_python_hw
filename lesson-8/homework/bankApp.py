import json
import random

class Account:

    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        acc_num = str(random.randint(10000, 99999))
        self.accounts[acc_num] = Account(acc_num, name, initial_deposit)
        self.save_to_file()
        return acc_num

    def view_account(self, acc_num):
        return self.accounts.get(acc_num, None)

    def deposit(self, acc_num, amount):
        account = self.view_account(acc_num)
        if account and account.deposit(amount):
            self.save_to_file()
            return True
        return False

    def withdraw(self, acc_num, amount):
        account = self.view_account(acc_num)
        if account and account.withdraw(amount):
            self.save_to_file()
            return True
        return False

    def save_to_file(self):
        with open("accounts.txt", "w") as f:
            json.dump({acc: vars(self.accounts[acc]) for acc in self.accounts}, f)

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as f:
                data = json.load(f)
                self.accounts = {acc: Account(**details) for acc, details in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}


bank = Bank()
while True:
    choice = input("\n1. Create Account\n2. View Account\n3. Deposit\n4. Withdraw\n5. Exit\nChoose: ")

    if choice == "1":
        name = input("Enter name: ")
        deposit = float(input("Initial deposit: "))
        print("Account Number:", bank.create_account(name, deposit))

    elif choice == "2":
        acc_num = input("Enter account number: ")
        acc = bank.view_account(acc_num)
        print(vars(acc) if acc else "Account not found.")

    elif choice == "3":
        acc_num = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        print("Deposit successful." if bank.deposit(acc_num, amount) else "Failed.")

    elif choice == "4":
        acc_num = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        print("Withdrawal successful." if bank.withdraw(acc_num, amount) else "Failed.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
