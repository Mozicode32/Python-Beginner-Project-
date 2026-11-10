class Inventory:
	def __init__(self):
		self.product={}
		
	def add_product(self):
		product = input('enter the product: ')
		quantity = int(input('enter quantity: '))
		self.product[product]=quantity
		
	def view_product(self):
		for product,quantity in self.product.items():
			print(f'{product} - {quantity}')
	
	def search_product(self):
		search = input('search product: ')
		if search in self.product:
			print(f''' {search}'s quantity is {self.product[search]}''')
			
	def update_quantity(self):
		pro = input('which product do you want to update: ')
		if pro in self.product:
			update = int(input('update quantity: '))
			if update > 0:
				self.product[pro]=update
				print(f'{pro} quantity have been updated to {update} ')
				
produce=Inventory()
while True:
	print('''
	====INVENTORY====
	1. add product
	2. view product
	3. search product
	4. update quantity 
	5. exit
	''')
	choose = int(input('choose what you want to do: '))
	if choose == 1:
		produce.add_product()
	elif choose == 2:
		produce.view_product()
	elif choose == 3:
		produce.search_product()
	elif choose == 4:
		produce.update_quantity()
	elif choose == 5:
		break
	else:
		print('invalid')
