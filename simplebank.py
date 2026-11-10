class BankAccount:
	def __init__(self,name,balance):
		self.name=name
		self.balance=balance
my_bank=BankAccount ('mozicode',10000)
print(f'name: {my_bank.name}')
print(f'balance: {my_bank.balance}')
while True:
    x=int(input('''
   1. check balance
   2. deposit
   3. withdraw 
   0. exit
        	
       : '''))
    if x==1:
    	print(my_bank.balance)
    elif x == 2:
    	deposit=int(input('amount: '))
    	if deposit < 0:
    		print('try again')
    		continue
    	my_bank.balance+=deposit
    	print('New balance: ',my_bank.balance)
    elif x == 3:
    	withdraw=int(input('amount: '))
    	if withdraw > my_bank.balance:
    		print('try again')
    		continue 
    	my_bank.balance-=withdraw
    	print('New balance: ',my_bank.balance)
    elif x == 0:
    	break
    else:
    	print('invalid')
