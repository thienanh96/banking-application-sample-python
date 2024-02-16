from domains.entities.account import Account
from domains.entities.customer import Customer
from domains.repositories.account_repository import AccountRepository
from domains.repositories.customer_repository import CustomerRepository


class AccountManagementUseCase:
    def __init__(self, account_repository: AccountRepository, customer_repository: CustomerRepository) -> None:
        self.account_repository: AccountRepository = account_repository
        self.customer_repository: CustomerRepository = customer_repository

    def create_account(self, customer_id: str | None, name: str | None, email: str | None, phone_number: str | None) -> Account:
        customer: Customer | None = None
        if customer_id:
            customer = self.customer_repository.find_by_id(customer_id)
        else:
            customer = Customer(
                self.customer_repository.next_identity(), name, email, phone_number)
            self.customer_repository.save(customer)

        account_id: str = self.account_repository.next_identity()
        account_number: str = self.account_repository.generate_account_number()
        account: Account = Account(account_id, customer.id, account_number)
        self.account_repository.save(account)
        return account
