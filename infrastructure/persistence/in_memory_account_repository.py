from domains.repositories.account_repository import AccountRepository
from domains.entities.account import Account
from domains.exceptions import AccountNotFoundError
from typing import Dict, Optional
import uuid


class InMemoryAccountRepository(AccountRepository):
    def __init__(self) -> None:
        self.accounts: Dict[str, Account] = {}

    def save(self, account: Account) -> None:
        self.accounts[account.id] = account

    def find_by_id(self, account_id: str) -> Optional[Account]:
        account = self.accounts.get(account_id)
        if not account:
            raise AccountNotFoundError(account_id)
        return account

    def next_identity(self) -> str:
        return str(uuid.uuid4())

    def generate_account_number(self) -> str:
        return f"ACC-{len(self.accounts) + 1:010d}"
