from domains.exceptions import InsufficientBalanceError, InvalidTransactionAmountError

class Account:
    def __init__(self, account_id: str, customer_id: str, account_number: str, balance: float = 0.0):
        self.id: str = account_id
        self.customer_id: str = customer_id
        self.account_number: str = account_number
        self.balance: float = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidTransactionAmountError()
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidTransactionAmountError()
        if amount > self.balance:
            raise InsufficientBalanceError()
        self.balance -= amount

    def get_balance(self):
        return self.balance
