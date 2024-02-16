from domains.exceptions import InvalidTransactionTypeError
from domains.repositories.account_repository import AccountRepository
from domains.repositories.transaction_repository import TransactionRepository
from domains.entities.transaction import Transaction, TransactionType


class TransactionUseCase:
    def __init__(self, account_repository: AccountRepository, transaction_repository: TransactionRepository) -> None:
        self.account_repository = account_repository
        self.transaction_repository = transaction_repository

    def execute(self, account_id: str, amount: float, transaction_type: TransactionType) -> None:
        account = self.account_repository.find_by_id(account_id)
        if transaction_type == TransactionType.DEPOSIT.value:
            account.deposit(amount)
        elif transaction_type == TransactionType.WITHDRAW.value:
            account.withdraw(amount)
        else:
            raise InvalidTransactionTypeError(transaction_type)

        transaction = Transaction(id=self.transaction_repository.next_identity(
        ), amount=amount, transaction_type=transaction_type, account_id=account.id)
        self.transaction_repository.save(transaction)

        self.account_repository.save(account)
