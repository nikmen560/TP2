from strings import *
from Customer import Customer
from File import File
# from data import customers

# data = customers
# def create_customer():
	# Customer.create_customer(data)
	# File.write(file_path)

customers = File.read('data.json', 'data.json')[0]

def change_customer():
	print(customerChangeInfo)
	Customer.change_customer(customers)

	
	

while True:

	print(mainMenu)
	userInput = int(input(" "))

	if userInput == 1:
		Customer.show_customer(customers)
		print(customerInfoMenu)

		userInput = int(input(""))
		if userInput == 1:
			change_customer()

		elif userInput == 2:
			Customer.create_customer(data=customers)

	# elif userInput == 2:
	#     print('')




