import json
import argparse
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added task: {title}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")


def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed['title']}")
    except IndexError:
        print("Invalid task number.")


def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done.")
    except IndexError:
        print("Invalid task number.")


def main():
    parser = argparse.ArgumentParser(description="To-Do List CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")

    subparsers.add_parser("list")

    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("index", type=int)

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("index", type=int)

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        mark_done(args.index)
    elif args.command == "delete":
        delete_task(args.index)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()


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
