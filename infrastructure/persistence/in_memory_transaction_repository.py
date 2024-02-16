from domains.repositories.transaction_repository import TransactionRepository
from domains.entities.transaction import Transaction
from typing import Dict
import uuid


class InMemoryTransactionRepository(TransactionRepository):
    def __init__(self) -> None:
        self.transactions: Dict[str, Transaction] = {}

    def save(self, transaction: Transaction) -> None:
        self.transactions[transaction.id] = transaction

    def find_by_id(self, transaction_id: str) -> Transaction | None:
        return super().find_by_id(transaction_id)

    def next_identity(self) -> str:
        return str(uuid.uuid4())
