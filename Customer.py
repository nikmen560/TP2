from db import customers
from strings import *


class Customer:
    def __init__(self, name, surname, address, id):
        self.name = name
        self.surname = surname
        self.address = address
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_address(self, address):
        self.address = address
