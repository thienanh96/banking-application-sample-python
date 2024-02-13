from abc import ABC, abstractmethod
from domains.entities.account import Account
from typing import Optional

class AccountRepository(ABC):
    @abstractmethod
    def save(self, account: Account) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, account_id: str) -> Optional[Account]:
        raise NotImplementedError

    @abstractmethod
    def next_identity(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def generate_account_number(self) -> str:
        raise NotImplementedError
