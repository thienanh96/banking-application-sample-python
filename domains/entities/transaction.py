from datetime import datetime
from enum import Enum

class TransactionType(Enum):
    DEPOSIT = 'deposit'
    WITHDRAW = "withdraw"

class Transaction:
    def __init__(self, id: str, amount: float, transaction_type: TransactionType, account_id: str, created_at: datetime = None):
        self.id = id
        self.amount = amount
        self.transaction_type = transaction_type
        self.account_id = account_id
        self.created_at = created_at if created_at is not None else datetime.now()

    def __repr__(self):
        return (f"Transaction(id={self.id}, amount={self.amount}, "
                f"transaction_type='{self.transaction_type}', account_id='{self.account_id}', "
                f"created_at={self.created_at.isoformat()})")
