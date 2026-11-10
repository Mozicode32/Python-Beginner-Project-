class ClassAttendence:
	def __init__(self):
		self.attendence={}
		self.no_absent=0
		self.no_present=0
		
	def add_student(self):
		name=input('''enter student's name: ''').lower()
		attendence=input('enter present or absent: ').lower()
		if name in self.attendence.keys():
			print(f'{name} have already been registered')
		else:
			if attendence == 'absent':
				self.no_absent+=1
			elif attendence == 'present':
			   self.no_present+=1
			else:
				print('please enter absent or present')
				return
		self.attendence[name]=attendence
		
	def view_attendence(self):
		for name,attend in self.attendence.items():
			print(f'name of student: {name} - attendence: {attend}')
			
	def search(self):
		search=input('search🔎: ').lower()
		if search in self.attendence.keys():
			print(f'{search} is {self.attendence[search]}')
			
	def summary(self):
		print(f'''
		amount of student present today = {self.no_present}
		amount of student absent today =  {self.no_absent}''')
		
		
attendence=ClassAttendence()
while True:
	print('''
	=====STUDENT ATTENDENCE MANAGEMENT SYSTEM=====
	1. add student
	2. view attendence
	3. search for student
	4. attendence summary
	5. exit
	''')
	choose=int(input('what do you want to do: '))
	match choose:
		case 1:
			attendence.add_student()
		case 2:
			attendence.view_attendence()
		case 3:
			attendence.search()
		case 4:
			attendence.summary()
		case 5:
			break
		case _:
			print('invalid')
