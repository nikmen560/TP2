from strings import *
from Customer import Customer

print(mainMenu)
userInput = int(input(" "))

if userInput == 1:
    Customer.showCustomer()
    print(customerInfoMenu)

    userInput = int(input(""))
    if userInput == 1:
        print("введите номер покупателя")
        userInput = int(input(" "))
        Customer.changeCustomer()


elif userInput == 2:
    print("")
