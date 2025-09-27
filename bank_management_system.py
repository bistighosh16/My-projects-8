import random
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(100000, 999999)  
        self.balance = 0.0
    def display_balance(self):
        print(f"Your current balance is: ${self.balance}")
    def credit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} has been credited to your account.")
        else:
            print("Please enter a valid amount.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            print("Please enter a valid amount.")
class BankSystem:
    def __init__(self):
        self.accounts = {}
    def create_account(self):
        name = input("Enter your name: ")
        account = BankAccount(name)
        self.accounts[account.account_number] = account
        print(f"Account created successfully! Your account number is: {account.account_number}")
    def get_account(self):
        account_number = int(input("Enter your account number: "))
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found!")
            return None
def main():
    bank_system = BankSystem()
    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            bank_system.create_account()
        elif choice == "2":
            account = bank_system.get_account()
            if account:
                while True:
                    print("\n--- Account Options ---")
                    print("1. View Balance")
                    print("2. Credit Money")
                    print("3. Withdraw Money")
                    print("4. Exit")
                    option = input("Choose an option: ")
                    if option == "1":
                        account.display_balance()
                    elif option == "2":
                        amount = float(input("Enter amount to credit: $"))
                        account.credit(amount)
                    elif option == "3":
                        amount = float(input("Enter amount to withdraw: $"))
                        account.withdraw(amount)
                    elif option == "4":
                        break
                    else:
                        print("Invalid option, please try again.")
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()
