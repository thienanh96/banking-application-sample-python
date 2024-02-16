from domains.repositories.customer_repository import CustomerRepository
from domains.entities.customer import Customer
from domains.exceptions import CustomerNotFoundError
from typing import Dict, Optional
import uuid


class InMemoryCustomerRepository(CustomerRepository):
    def __init__(self) -> None:
        self.customers: Dict[str, Customer] = {}

    def save(self, customer: Customer) -> None:
        self.customers[customer.id] = customer

    def find_by_id(self, customer_id: str) -> Optional[Customer]:
        customer = self.customers.get(customer_id)
        if not customer:
            raise CustomerNotFoundError(customer_id)
        return customer

    def next_identity(self) -> str:
        return str(uuid.uuid4())
