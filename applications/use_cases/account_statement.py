from domains.repositories.account_repository import AccountRepository

class AccountStatementUseCase:
    def __init__(self, account_repository: AccountRepository) -> None:
        self.account_repository: AccountRepository = account_repository

    def generate(self, account_id: str) -> str:
        account = self.account_repository.find_by_id(account_id)
        return f"Account Statement for {account_id}: Balance = {account.get_balance()}"
