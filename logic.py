from strings import *
from db import customers
from Customer import Customer
# from data import customers

# data = customers
# def create_customer():
	# Customer.create_customer(data)
	# File.write(file_path)

def create_customer():
	customer_name = input('введите имя ')
	customer_surname = input('введите фамилию ')
	customer_address = input('введите адрес ')
	customer_id = len(customers)
	new_customer = Customer(customer_name,customer_surname,customer_address, customer_id)
	customers.append(new_customer.__dict__)

def change_customer(id):
	for customer in customers:
			if customer['id'] == id:
				print(customer)
				print("выберите что хотите сделать")
				print(customerChangeInfo)
				user_input = int(input(" "))

				if user_input == 1:
					print(enter_new_name)
					user_input = input(" ")
					customer['name'] = user_input

				elif user_input == 2:
					print(enter_new_surname)
					user_input = input(" ")
					customer['surname'] = user_input	

				elif user_input == 3:
					print(enter_new_address)
					user_input = input(" ")
					customer['address'] = user_input

def show_customers():
	print(devider)

	# read from file all customers

	for customer in customers:
		print(f"#{customer['id'] + 1} - {customer['name']} {customer['surname']} address: {customer['address']}")


print(mainMenu)
userInput = int(input(" "))

if userInput == 1:
	show_customers()
	print(customerInfoMenu)

	userInput = int(input(""))
	if userInput == 1:
		print("введите номер покупателя")
		show_customers()
		userInput = int(input(" ")) - 1
		change_customer(id=userInput)

	elif userInput == 2:
		create_customer()

# elif userInput == 2:
#     print('')
