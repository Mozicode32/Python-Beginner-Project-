class Library:
	def __init__(self,opt,name):
		self.opt=opt
		self.book=[]
		
	def collection(self):
		x=('''
		    1. Add book
		    2. Display books
		    3. Borrow book
		    4. Return book
		    5. Exit 
		    ''')
		print(x)
		option=int(input('choose any options: '))
		if option == 1:
			up=input('what is the name of the book you want to add: ')
			self.book.append(up)
		elif option == 2:
			print(self.book)
		elif option == 3:
			borrow = input('which of the book do you need: ')
			self.book.remove(borrow)
			print(self.book)
		elif option == 4:
			retur = input('which of the books do you want to return: ')
			self.book.append(retur)
			print(self.book)
		elif option == 5:
			return False
		else:
			print('not part of what we have')

books=Library('option','up')
while True:
	if books.collection() == False:
		break
    
