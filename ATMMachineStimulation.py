class ATMMachine:
    def __init__(self):
        self.balance = 1000.0  # Initial balance
        self.pin = 8576  # Simulated PIN for validation

    def display_menu(self):
        print("\nATM Machine")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def check_pin(self):
        for attempt in range(5):  # Allow 5 attempts to enter the correct PIN
            entered_pin = int(input("Enter your 4-digit PIN: "))
            if entered_pin == self.pin:
                return True
            else:
                print(f"Incorrect PIN. You have {2 - attempt} attempt(s) left.")
        return False

    def check_balance(self):
        print(f"Your current balance is: rupees{self.balance:.2f}")

    def deposit_money(self):
        deposit_amount = float(input("Enter the amount to deposit: rupees"))
        if deposit_amount > 0:
            self.balance += deposit_amount
            print(f"Successfully deposited rupees{deposit_amount:.2f}. New balance: rupees{self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw_money(self):
        withdraw_amount = float(input("Enter the amount to withdraw: rupees"))
        if withdraw_amount > 0 and withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print(f"Successfully withdrew rupees{withdraw_amount:.2f}. Remaining balance: rupees{self.balance:.2f}")
        elif withdraw_amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdraw amount. Please enter a positive value.")

    def run(self):
        if not self.check_pin():
            print("Too many incorrect PIN attempts. Exiting...")
            return

        while True:
            self.display_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit_money()
            elif choice == '3':
                self.withdraw_money()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

# Run the ATM simulation
if __name__ == "__main__":
    atm = ATMMachine()
    atm.run()
