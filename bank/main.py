from models.Client import ClientType, Client
from models.Account import AccountType, Account

client_id = 1
account_id = 1
clients = {}

def client_menu():
	global client_id, clients

	while True:
		print("\n[1] List clients")
		print("[2] Create personal client")
		print("[3] Create business client")
		print("[4] Select client")
		print("[5] Exit")
		option = input("Option: ")
		match option:
			case "1":
				print()
				if len(clients) == 0:
					print("No clients were found.")
				else:
					for c in clients.values(): print(c)
			case "2" | "3":
				name = input("\nname: ")
				address = input("address: ")
				type = ClientType.PERSONAL if option == "2" else ClientType.BUSINESS
				clients[client_id] = Client(type, client_id, name, address)
				client_id += 1
			case "4":
				id = int(input("\nClient id: "))
				client = clients.get(id)
				if not client:
					print("Invalid id!")
				else:
					account_menu(client)
			case "5":
				break
			case _:
				print("\nInvalid option!")

def account_menu(client: Client):
	global account_id

	while True:
		print("\n[1] List accounts")
		print("[2] Create saving account")
		print("[3] Create checkout account")
		print("[4] Select account")
		print("[5] Back")
		option = input("Option: ")
		match option:
			case "1":
				print()
				if len(client.accounts) == 0:
					print("No accounts were found.")
				else:
					for a in client.accounts.values(): print(a)
			case "2" | "3":
				type = AccountType.SAVINGS if option == "2" else AccountType.CHECKING
				client.add_account(Account(type, account_id))
				account_id += 1
			case "4":
				id = int(input("\nAccount id: "))
				account = client.accounts.get(id)
				if not account:
					print("Invalid id!")
				else:
					operation_menu(account)
			case "5":
				break
			case _:
				print("\nInvalid option!")

def operation_menu(account: Account):
	while True:
		print("\n[1] Statement")
		print("[2] Deposit")
		print("[3] Withdraw")
		print("[4] Back")
		option = input("Option: ")
		match option:
			case "1":
				print()
				account.statement()
			case "2":
				amount = float(input("\namount: "))
				account.deposit(amount)
			case "3":
				amount = float(input("\namount: "))
				account.withdraw(amount)
			case "4":
				break
			case _:
				print("\nInvalid option!")

client_menu()
