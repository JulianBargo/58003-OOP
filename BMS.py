import tkinter as tk

class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_deposit):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_deposit

class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.bank_accounts = []

class Bank:
    def __init__(self):
        self.users = []

    def create_user(self):
        name = name_entry.get()
        address = address_entry.get()
        user = User(name, address)
        self.users.append(user)
        result_label.config(text=f"User {name} created successfully.")

    def create_account(self):
        name = name_entry.get()
        account_number = account_number_entry.get()
        initial_deposit = float(initial_deposit_entry.get())
        user = self.find_user(name)
        if user:
            account = BankAccount(account_number, user.name, initial_deposit)
            user.bank_accounts.append(account)
            result_label.config(text=f"Account created successfully. Account number: {account_number}")
        else:
            result_label.config(text=f"User {name} does not exist.")

    def deposit(self):
        name = name_entry.get()
        account_number = account_number_entry.get()
        amount = float(amount_entry.get())
        user = self.find_user(name)
        if user:
            account = self.find_account(user, account_number)
            if account:
                account.balance += amount
                result_label.config(text=f"Amount {amount} deposited. Current balance: {account.balance}")
            else:
                result_label.config(text=f"Account {account_number} does not exist.")
        else:
            result_label.config(text=f"User {name} does not exist.")

    def withdraw(self):
        name = name_entry.get()
        account_number = account_number_entry.get()
        amount = float(amount_entry.get())
        user = self.find_user(name)
        if user:
            account = self.find_account(user, account_number)
            if account:
                if account.balance >= amount:
                    account.balance -= amount
                    result_label.config(text=f"Amount {amount} withdrawn. Current balance: {account.balance}")
                else:
                    result_label.config(text="Insufficient funds.")
            else:
                result_label.config(text=f"Account {account_number} does not exist.")
        else:
            result_label.config(text=f"User {name} does not exist.")

    def check_balance(self):
        name = name_entry.get()
        account_number = account_number_entry.get()
        user = self.find_user(name)
        if user:
            account = self.find_account(user, account_number)
            if account:
                result_label.config(text=f"Account balance: {account.balance}")
            else:
                result_label.config(text=f"Account {account_number} does not exist.")
        else:
            result_label.config(text=f"User {name} does not exist.")

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def find_account(self, user, account_number):
        for account in user.bank_accounts:
            if account.account_number == account_number:
                return account
        return None


# Create the bank object
bank = Bank()

# Create the main window
root = tk.Tk()
root.title("Bank Application")

# Create labels
name_label = tk.Label(root, text="Name:")
address_label = tk.Label(root, text="Address:")
account_number_label = tk.Label(root, text="Account Number:")
initial_deposit_label = tk.Label(root, text="Initial Deposit:")
amount_label = tk.Label(root, text="Amount:")
result_label = tk.Label(root, text="")

# Create entry fields
name_entry = tk.Entry(root)
address_entry = tk.Entry(root)
account_number_entry = tk.Entry(root)
initial_deposit_entry = tk.Entry(root)
amount_entry = tk.Entry(root)

# Create buttons
create_user_button = tk.Button(root, text="Create User", command=bank.create_user)
create_account_button = tk.Button(root, text="Create Account", command=bank.create_account)
deposit_button = tk.Button(root, text="Deposit", command=bank.deposit)
withdraw_button = tk.Button(root, text="Withdraw", command=bank.withdraw)
check_balance_button = tk.Button(root, text="Check Balance", command=bank.check_balance)

# Arrange the widgets using the grid layout manager
name_label.grid(row=0, column=0, sticky="e")
name_entry.grid(row=0, column=1)
address_label.grid(row=1, column=0, sticky="e")
address_entry.grid(row=1, column=1)
create_user_button.grid(row=2, column=0, columnspan=2)
account_number_label.grid(row=3, column=0, sticky="e")
account_number_entry.grid(row=3, column=1)
initial_deposit_label.grid(row=4, column=0, sticky="e")
initial_deposit_entry.grid(row=4, column=1)
create_account_button.grid(row=5, column=0, columnspan=2)
amount_label.grid(row=6, column=0, sticky="e")
amount_entry.grid(row=6, column=1)
deposit_button.grid(row=7, column=0, columnspan=2)
withdraw_button.grid(row=8, column=0, columnspan=2)
check_balance_button.grid(row=9, column=0, columnspan=2)
result_label.grid(row=10, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
