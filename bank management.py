import json
from pathlib import Path

DATA_FILE = Path("accounts.json")


def load_accounts():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_accounts(accounts):
    with open(DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=2)


def create_account(accounts):
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    accounts[acc_no] = {"name": name, "balance": balance}
    save_accounts(accounts)
    print("Account created successfully!")


def view_account(accounts):
    acc_no = input("Enter account number: ")
    account = accounts.get(acc_no)

    if not account:
        print("Account not found.")
        return

    print("\n--- Account Details ---")
    print(f"Account No: {acc_no}")
    print(f"Name: {account['name']}")
    print(f"Balance: {account['balance']}")


def deposit(accounts):
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter deposit amount: "))
    accounts[acc_no]["balance"] += amount
    save_accounts(accounts)
    print("Deposit successful.")


def withdraw(accounts):
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter withdrawal amount: "))
    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance.")
        return

    accounts[acc_no]["balance"] -= amount
    save_accounts(accounts)
    print("Withdrawal successful.")


def delete_account(accounts):
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        del accounts[acc_no]
        save_accounts(accounts)
        print("Account deleted.")
    else:
        print("Account not found.")


def main():
    accounts = load_accounts()

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Delete Account")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            view_account(accounts)
        elif choice == "3":
            deposit(accounts)
        elif choice == "4":
            withdraw(accounts)
        elif choice == "5":
            delete_account(accounts)
        elif choice == "6":
            print("Thank you for using the Bank System 👋")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
