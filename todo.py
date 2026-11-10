class Todo:
	def __init__(self):
		self.task=[]
	def add_tasks(self):
			add = input('add tasks: ')
			self.task.append(add)
	def view_tasks(self):
			for i in self.task:
				print(i)
	def remove_tasks(self):
			task = input('what tasks do you want to remove: ')
			self.task.remove(task)
			
			
tasked=Todo()
print('''
	1. add tasks
	2. view task
	3. remove tasks
	4. exit''')
while True:
	choose=int(input('what do you want to do: '))
	if choose == 1:
		tasked.add_tasks()
		print()
	elif choose == 2:
		tasked.view_tasks()
		print()
	elif choose == 3:
		tasked.remove_tasks()
		print()
	elif choose == 4:
		break
	else:
		print('not in the list')
