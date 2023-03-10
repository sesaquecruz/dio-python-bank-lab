from enum import Enum

from models.Account import Account

class ClientType(Enum):
    PERSONAL = 1
    BUSINESS = 2

class Client:
	def __init__(self, type: ClientType, id: str, name: str, address: str):
		self.type = type
		self.id = id
		self.name = name
		self.address = address
		self.accounts = {}

	def add_account(self, account: Account) -> bool:
		if self.accounts.get(account.id):
			print("Operation failed! - Account already registered.")
			return False
		self.accounts[account.id] = account
		return True

	def __str__(self) -> str:
		return f"{self.type.name} - {self.id}, {self.name}, {self.address}"
