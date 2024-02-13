from infrastructure.persistence.in_memory_account_repository import InMemoryAccountRepository
from infrastructure.persistence.in_memory_customer_repository import InMemoryCustomerRepository
from applications.use_cases.account_management import AccountManagementUseCase
from applications.use_cases.transaction import TransactionUseCase
from applications.use_cases.account_statement import AccountStatementUseCase
from domains.exceptions import InsufficientBalanceError
import uuid


if __name__ == '__main__':
    # Setup the infrastructure layer
    account_repository = InMemoryAccountRepository()
    customer_repository = InMemoryCustomerRepository()

    # Initialize use cases with the repository
    account_management_use_case = AccountManagementUseCase(account_repository, customer_repository)
    transaction_use_case = TransactionUseCase(account_repository)
    account_statement_use_case = AccountStatementUseCase(account_repository)

    # Demonstrate creating customer and account
    account = account_management_use_case.create_account(None, 'John Doe', 'john@example.com', '555-1234')
    print(f"Account {account.account_number} created for customer {account.customer_id}")

    # Demonstrate making transactions
    try:
        transaction_use_case.execute(account.account_id, 100, 'deposit')
        transaction_use_case.execute(account.account_id, 50, 'withdraw')
        print("Transactions completed successfully.")
    except InsufficientBalanceError as e:
        print(f"Transaction failed: {e}")

    # Demonstrate generating an account statement
    statement = account_statement_use_case.generate(account.account_id)
    print(statement)
