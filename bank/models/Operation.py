from enum import Enum
from datetime import datetime

class OperationType(Enum):
	DEPOSIT = 1
	WITHDRAW = 2

class Operation:
	def __init__(self, type: OperationType, date: datetime, amount: float):
		self.type = type
		self.date = date
		self.amount = amount

	def __str__(self) -> str:
		return f"{self.type.name} - {self.date.strftime('%Y/%m/%d')}, $ {self.amount:.2f}"
