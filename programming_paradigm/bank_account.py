class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount with an initial balance.
        If no balance is provided, the value will be 0
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit an amount to the account balance
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a certain amount from the account if sufficient balance exists.
        Returns True if successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self):
        """
        Print the current balance of the account in a friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
