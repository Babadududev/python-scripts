class BankAccount: 
    def __init__ (self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    #method to deposit:
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"you deposited ${amount: .2f} into your account successfully, new balance is ${self.balance: .2f}")
        else:
            print("Enter a positive amount, please.")

    #method to withdraw:
    def withdraw(self, amount: float):
        if amount <0:
            print("please enter a positive amount.")
        elif amount > self.balance :
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Your account has been debited successfully, your new balance is ${self.balance: .2f}")

    #method to get balance:
    def get_balance(self):
        return self.balance

    #method to display info:
    def display_info(self):
        print(f"\n Account Owner: {self.owner}")
        print(f"Account Balance: {self.balance}\n")

if __name__ == "__main__":

    account = BankAccount("Victoria", 100000.0)

    # Display initial state
    account.display_info()

    # Perform operations
    account.deposit(50.0)
    account.withdraw(30.0)
    account.withdraw(200.0)  # Handles insufficient balance

    # Final balance check
    account.display_info()




