from strings import *
from db import customers
from Customer import Customer
# from data import customers

# data = customers
# def create_customer():
    # Customer.create_customer(data)
    # File.write(file_path)

def create_customer():
    customer_name = input('введите имя')
    customer_surname = input('введите фамилию')
    customer_address = input('введите адрес')
    new_customer = Customer(customer_name,customer_surname,customer_address)
    customers.append(new_customer.__dict__)
    show_customers()

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
        Customer.showCustomer()
        userInput = int(input(" ")) - 1
        Customer.changeCustomer(id=userInput)
    elif userInput == 2:
        create_customer()

# elif userInput == 2:
#     print('')
