from db import customers
from strings import *


class Customer:
    def __init__(self, name, surname, address, id=None) -> None:
        self.name = name
        self.surname = surname
        self.address = address
        self.id = id

    def __set_name__(self, name):
        self.name = name

    def __set_surname__(self, surname):
        self.surname = surname

    def __set_address__(self, address):
        self.address = address

    def changeCustomer(id):
        for customer in customers:
            if customer['id'] == id:
                print(customer)
                print("выберите что хотите сделать")
                print(customerChangeInfo)
                userInput = int(input(" "))
                if userInput == 1:
                    print("you changed name")
                # changeCustomerName(customer)
