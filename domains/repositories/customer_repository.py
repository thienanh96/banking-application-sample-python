from abc import ABC, abstractmethod
from domains.entities.customer import Customer
from typing import Optional

class CustomerRepository(ABC):
    @abstractmethod
    def save(self, customer: Customer) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, customer_id: str) -> Optional[Customer]:
        raise NotImplementedError

    @abstractmethod
    def next_identity(self) -> str:
        raise NotImplementedError