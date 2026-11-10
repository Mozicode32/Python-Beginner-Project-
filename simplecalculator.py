class Calculator:
	def __init__(self):
		self.history=[]
		
		
	def calculate(self):
		print('''
	1. calculate 
	2. exit
	3. history''')
		x=int(input('choose: '))
		if x == 1:
			y=int(input('enter the first number: '))
			z=int(input('enter the second number: '))
			print()
			u=input('operator:  ')
			if u == '+':
				print(f'answer = {y+z}')
				self.history.append(f'{y} + {z} = {y+z}')
			elif u == '*':
				print(f'answer = {y*z}')
				self.history.append(f'{y} * {z} = {y*z}')
			elif u == '/':
				print(f'answer = {y/z}')
				self.history.append(f'{y} / {z} = {y/z}')
			elif u == '-':
				print(f'answer = {y-z}')
				self.history.append(f'{y} - {z} = {y-z}')
				print()
		elif x == 2:
			return False
		elif x == 3:
			print('----CALCULATION HISTORY----')
			
			for calculate in self.history:
				print(calculate)
		else:
			print('please choose 1 or 2')
cal=Calculator()			
while True:
	if cal.calculate() == False:
		break
