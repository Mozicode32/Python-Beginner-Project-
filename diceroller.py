from random import randint
class DiceRoller:
	def roll(self):
		print('''
		🎲 DICE ROLLER
		
		1. roll dice
		2. exit
		''')
		choose = int(input('what do you want to do: '))
		if choose == 1:
		   	dice = int(input('how many dice do you want to roll: '))
		   	for i in range(dice):
		   		print(f'you rolled: {randint(1,6)} 🎲')
		elif choose == 2:
			return False
		else:
			print('not in the list')
			
			
dice=DiceRoller()
while True:
	if dice.roll() == False:
		break
