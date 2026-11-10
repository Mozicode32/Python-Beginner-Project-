class BankTracker:
	def __init__(self):
		self.bank={}
		
	def create_account(self):
		name = input('enter customer name: ')
		balance = int(input('enter customer starting balance: '))
		if balance >= 500:
			self.bank[name]=balance
		else:
				print('''please you can't enter any amount less the $500''')
	
	def veiw_account(self):
		for name,bals in self.bank.items():
			print(f'{name} - ${bals}')
			
	def check_balance(self):
		check = input('''which customer's balance do you what to check: ''')
		if check in self.bank:
			print(f'''{check}'s balance is ${self.bank[check]}''')
		else:
			print('not in our list')
			
	def deposit(self):
		cust = input('enter customer name: ')
		if cust in self.bank:
			deposit = int(input('amount to deposit: '))
			if deposit > 0:
				self.bank[cust]+=deposit
			else:
					print('''you can't deposit a negative number''')
		else:
			print('not in list')
			
	def withdraw(self):
		cust = input('''which customer's account what to be withdrawn from: ''')
		if cust in self.bank:
			withdrawal_amount = int(input('enter withdrawal amount: '))
			if withdrawal_amount >=100:
				if withdrawal_amount > self.bank[cust]:
					print('insuficient fund')
				else:
					self.bank[cust]-=withdrawal_amount
			else:
				print('Minimium withdrawal is $100')
		else:
			print('customer not in list')
	
account = BankTracker()
while True:
	print('''
	=====BANK TRACKER=====
	  1. create account. 
	  2. veiw account.
	  3. check balance.
	  4. deposit.
	  5. withdraw.
	  6. exit.
	  ''')
	choose = int(input('choose what you want to do: '))
	if choose == 1:
		account.create_account()
	elif choose == 2:
		account.veiw_account()
	elif choose == 3:
		account.check_balance()
	elif choose == 4:
		account.deposit()
	elif choose == 5:
		account.withdraw()
	elif choose == 6:
		break
	else:
		print('invalid')
