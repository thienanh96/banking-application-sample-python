from abc import ABC, abstractmethod
from domains.entities.transaction import Transaction
from typing import Optional


class TransactionRepository(ABC):
    @abstractmethod
    def save(self, transaction: Transaction) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, transaction_id: str) -> Optional[Transaction]:
        raise NotImplementedError

    @abstractmethod
    def next_identity(self) -> str:
        raise NotImplementedError
