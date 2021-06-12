from db import customers
from strings import *


class Customer:
	def __init__(self, name, surname, address, id):
		self.name = name
		self.surname = surname
		self.address = address
		self.id = id

  

	def create_customer(data):
		customer_name = input(create_new_customer_name)
		customer_surname = input(create_new_customer_surname)
		customer_address = input(create_new_customer_address)
		customer_id = len(customers)
		new_customer = Customer(customer_name,customer_surname,customer_address, customer_id)
		customers.append(new_customer)

		return new_customer

	def choose_customer(data):
		Customer.show_customer(data)
		user_input = int(input('введите номер покупателя'))
		id = user_input - 1 

		for customer in data:
			if customer.id == id:
				return customer

	def show_customer(data):
		for customer in data:
			print(f"#{customer['id'] + 1} - {customer['name']} {customer['surname']} address: {customer['address']}")
	
	def change_customer(data):
		customer = Customer.choose_customer(data)

		user_choice = input(customerChangeInfo)
		if int(user_choice) == 1:
			customer.name = input(customer_new_name)
		
		elif int(user_choice) == 2:
			customer.surname == input(customer_new_surname)
		
		elif int(user_choice) == 3:
			customer.address == input(customer_new_address)