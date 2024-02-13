class InvalidTransactionAmountError(Exception):
    def __init__(self, message="Transaction amount must be positive"):
        super().__init__(message)

class InvalidTransactionTypeError(Exception):
    def __init__(self, transaction_type: str, message="Invalid transaction type"):
        super().__init__(f"{message}: {transaction_type}")

class InsufficientBalanceError(Exception):
    """Exception raised when an account has insufficient balance for a withdrawal."""
    def __init__(self, message="Insufficient balance for the transaction"):
        self.message = message
        super().__init__(self.message)

class AccountNotFoundError(Exception):
    """Exception raised when an account is not found."""
    def __init__(self, account_id, message="Account not found"):
        self.account_id = account_id
        self.message = f"{message}: {account_id}"
        super().__init__(self.message)

class CustomerNotFoundError(Exception):
    """Exception raised when a customer is not found."""
    def __init__(self, customer_id, message="Customer not found"):
        self.customer_id = customer_id
        self.message = f"{message}: {customer_id}"
        super().__init__(self.message)
