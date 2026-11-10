class ScoreTracker:
	def __init__(self):
		self.score={}
		self.count=0
		
	def add_student(self):
		name=input('''enter student's name: ''')
		score=int(input('''enter student's score: '''))
		if score >= 0:
			self.count+=1
			self.score[name]=score
		else:
			print('''can't enter a negetive number''')
			
	def view_student(self):
		for name,score in self.score.items():
			print(f'name: {name} - score: {score}')
			
	def search_student(self):
		search=input('search student: ')
		if search in self.score.keys():
			print(f'''{search}'s score is {self.score[search]}''')
		else:
			print('student not found')
	def cal_average(self):
		no=0
		if self.count <= 0:
				print('you have not added any student')
		else:
			for val in self.score.values():
				no+=val
			print(f'average = {no/self.count}')
		
		
score=ScoreTracker()
while True:
	print('''
	====SCORE TRACKER====
	    1. add student
	    2. view student
	    3. search student
	    4. average 
	    5. exit
	    ''')
	choose=int(input('choose what you want to do: '))
	if choose == 1:
		score.add_student()
	elif choose== 2:
		score.view_student()
	elif choose == 3:
		score.search_student()
	elif choose == 4:
		score.cal_average()
	elif choose == 5:
		break
	else:
		print('invalid')
