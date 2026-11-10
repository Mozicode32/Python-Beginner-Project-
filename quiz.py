class Quiz:
	def __init__(self):
		self.score=0
	def question(self):
		print('welcome to the quiz: ')
		print()
		print('''question .1
what is the function of red blood cell in our body.
		a.)it kill bacteria.
		b.)it carry oxygen to every part of the body.
		c.)it helps in the production of food.
		d.)it is poisonous.''')
		x = input('choose the right answer: ')
		if x == 'b':
			print('correct🎉🎉')
			self.score+=1
			print('your score is :',self.score)
		else:
			print('not correct')
		print()
		print('''question 2.
what is the aventage of friction.
		a.)it help us to sleep.
		b.)it help us to fly like chickens.
		c.)it help us to stand fame on the ground.
		d.)it provide free food.''')
		y = input('choose the right answer: ')
		if y == 'c':
			print('correct🎉🎉')
			self.score+=1
			print('your score is :',self.score)
		else:
			print('not correct')
			
			
quiz=Quiz()
quiz.question()
