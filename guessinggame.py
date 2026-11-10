class GuessingGame:
	def __init__(self,name):
		self.name=name
		self.count=0
		choose=input('enter your name: ')
		print(f'''welcome {choose}!!  i'm thinking of a number between 1 and 20''')
	def guess(self):
		self.count+=1
		print()
		no=12
		x=int(input('guess the number: '))
		if x == no:
			print('correct 🎉🎉')
		elif x > no:
			print('too high')
		else:
			print('too low')
		print(f'you have made {self.count} attempts')
attempt=GuessingGame('choose',)
while attempt.count < 3:
	attempt.guess()
