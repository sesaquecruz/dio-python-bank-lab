from enum import Enum
from datetime import datetime

from models.Operation import OperationType, Operation

class AccountType(Enum):
	SAVINGS = 1
	CHECKING = 2

class Account:
	def __init__(self, type: AccountType, id: str):
		self.type = type
		self.id = id
		self.balance = 0.0
		self.operations = []

	def find_operations(self, year: int, month: int, day: int) -> list:
		return [o for o in self.operations if (o.date.year == year and o.date.month == month and o.date.day == day)]

	def deposit(self, amount: float) -> bool:
		if amount <= 0:
			print("Operation failed! - Invalid amount.")
			return False
		date = datetime.now()
		self.balance += amount
		self.operations.append(Operation(OperationType.DEPOSIT, date, amount))
		return True

	def withdraw(self, amount: float) -> bool:
		if amount <= 0 or amount > 500 or amount > self.balance:
			print("Operation failed! - Invalid amount.")
			return False
		date = datetime.now()
		withdraws = [o for o in self.find_operations(date.year, date.month, date.day) if (o.type == OperationType.WITHDRAW)]
		if len(withdraws) >= 3:
			print("Operation failed! - Limite exceeded.")
			return False
		self.balance -= amount
		self.operations.append(Operation(OperationType.WITHDRAW, date, amount))
		return True

	def statement(self) -> None:
		if len(self.operations) == 0:
			print("There were no transactions")
		else:
			for o in self.operations:
				print(o)
		print(f"Balance - $ {self.balance:.2f}")

	def __str__(self) -> str:
		return f"{self.type.name} - {self.id}, $ {self.balance}"
