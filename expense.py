class ExpensesTracker:
	def __init__(self):
		self.expense={}
		
	def add(self):
		name=input('enter name: ')
		price=int(input('amount: '))
		self.expense[name]=price
			
	def view_expenses(self):
		for name,price in self.expense.items():
			print(f'{name} - ${price}')

	def total(self):
			total=0
			for price in self.expense.values():
				total+=price
			print(f'total: ${total}')
	
expense=ExpensesTracker()
while True:
	print('''====EXPENSES TRACKER====
	      1. add expenses
	      2. view expenses
	      3. view total expenses
	      4. exit
	            ''')
	choose = int(input('what do you want to do: '))
	if choose == 1:
		expense.add()
	elif choose == 2:
		expense.view_expenses()
	elif choose == 3:
		expense.total()
	elif choose == 4:
		break
	else:
		print('enter a number again')
