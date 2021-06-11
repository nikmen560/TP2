from data import *
from strings import *


class Customer:
	def __init__(self, name, surname, address, id=None) -> None:
		self.name = name
		self.surname = surname
		self.address = address
		self.id = id

	@staticmethod
	def showCustomer():
		#	userInput = int(input("введите id пользователя"))
		print(devider)
		for customer in customers:
			print(f"#{customer['id'] + 1} - {customer['name']} {customer['surname']} address: {customer['address']}")

	def changeCustomer(self, id):
		for customer in customers:
			if customer['id'] == id:
				print()