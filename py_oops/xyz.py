class Atm:
    def __init__(self):
        self.balance = 0
        self.pin = None
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
1. Sign up
2. Login
3. Exit
""")
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                if self.verify_pin():
                    self.transaction_menu()
            elif user_input == "3":
                print("Thank you for using our ATM!")
                break
            else:
                print("Invalid option, please try again")

    def transaction_menu(self):
        while True:
            user_input = input("""
1. Deposit money
2. Withdraw
3. Check balance
4. Logout
""")
            if user_input == "1":
                self.deposit_money()
            elif user_input == "2":
                self.withdraw_money()
            elif user_input == "3":
                print("Your balance is:", self.check_balance())
            elif user_input == "4":
                break
            else:
                print("Invalid option, please try again")

    def create_pin(self):
        self.pin = int(input("Set your pin: "))
        print("PIN created successfully!")

    def verify_pin(self):
        if self.pin is None:
            print("No PIN exists. Please sign up first.")
            return False
        entered_pin = int(input("Enter your PIN: "))
        if entered_pin == self.pin:
            return True
        print("Incorrect PIN!")
        return False

    def deposit_money(self):
        amount = int(input("Deposit amount: "))
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid amount")

    def withdraw_money(self):
        amount = int(input("Withdraw amount: "))
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid amount or insufficient balance")

    def check_balance(self):
        return self.balance

bob = Atm()