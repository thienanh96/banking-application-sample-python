from domains.exceptions import InvalidTransactionTypeError

class TransactionUseCase:
    def __init__(self, account_repository) -> None:
        self.account_repository = account_repository

    def execute(self, account_id: str, amount: float, transaction_type: str) -> None:
        account = self.account_repository.find_by_id(account_id)
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)
        else:
            raise InvalidTransactionTypeError(transaction_type)
        self.account_repository.save(account)
