# function:   validate
# input:      (1) a string to prompt the user with ('Enter a number: ')
#             (2) a data type (string) - either 'float' or 'integer'
#                 default this value to 'float' if none is supplied
#             (3) the lowest possible number you can accept as part of
#                 your validation (integer) - default to the string "unlimited"
#                 if no integer is provided
#             (4) the highest possible number you can accept as part of
#                 your validation (integer) - default to the string "unlimited"
#                 if no integer is provided
#
#             note: you can tell Python to assign a 'default' value to an argument
#             by using this syntax in your function definition:
#
#             def foo(a, b, c="hello", d=57)
#
#             in this case 'a' and 'b' are required arguments and must be supplied
#             'c' and 'd' are optional, and if they are not supplied they will be
#             assigned the values 'hello' and 57 respectively.  for example:
#
#             foo(10, 20) # function receives a=10 b=20 c="hello" d=57
#             foo(10, 20, 30)  # function receives a=10, b=20 c=30, d=57
#             foo(10, 20, 30, 40)  # function receives a=10, b=20 c=30 d=40
#
# processing: continually prompts the user with the prompt provided. the user's
#             input will be convereted to the data type requested.  if the data type
#             conversion results in a runtime error the program should not crash but
#             but alert the user with a print statement (i.e. Not a number, try again")
#             if the result is successful the function will ensure that it falls within
#             the bounds provided.
# output:     returns the validated user input (float or int)
import math

def validate(prompt, datatype="float", low="unlimited", high="unlimited"):
    if low == "unlimited":
        low = -math.inf
    if high == "unlimited":
        high = math.inf
    value = input(prompt)
    while True:
        if datatype == "float":
            try:
                float(value)
            except:
                print("Not a number, try again")
            else:
                value = float(value)
                if value > high or value < low:
                    print("Invalid range, try again")
                    value = input(prompt)
                    continue
                break
        if datatype == "integer":
            try:
                int(value)
            except:
                print("Not a number, try again")
            else:
                value = int(value)
                if value > high or value < low:
                    print("Invalid range, try again")
                    value = input(prompt)
                    continue
                break
        value = input(prompt)
    return value

# I make the original menu using a dictionary
inventory = {
                'soft drink': [0.99, 10],
                'onion rings': [1.29, 5],
                'small fries': [1.49, 20]
            }

# Made an infinite loop until broken
while True:
# I ask the user for an option input and data validate it
    option = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
    if option != "s" and option != "l" and option != "a" and option != "r" and option != "u" and option != "e" and option != "q":
        print("Unknown command, try again")

# If the option is s I will ask the user for a product name and if it exists
# I will print out the price of that product
    if option == "s":
        product = input("Enter a product name: ")
        if product in inventory:
            print("We sell '", product, "' at ", inventory[product][0], " per unit", sep="")
        else:
            print("Sorry, we don't sell '", product, "'", sep="")
# If the option is l then I will list out all the products in the dictionary
# in a table format 
    if option == "l":
        print(format("Product", '<21s'), format("Price", '<8s'), format("Quantity", '<5s'))
        for product in inventory:
            x = format(inventory[product][0], '.2f')
            print(format(product, '<21s'), format(str(x), '<8s'), format(str(inventory[product][1]), '<5s'))
# If the option is a then the user can input a new product name and if it doesn't
# already exist then they can add a price and the # of stock to it to add it to the
# dictionary
    if option == "a":
        newproductname = input("Enter a new product name: ")
        if newproductname in inventory:
            print("Duplicate product name")
            continue
        newproductcost = float(input("Enter a product cost: "))
        while newproductcost <= 0:
            print("Invalid range, try again.")
            newproductcost = float(input("Enter a product cost: "))
        newproductstock = int(input("How many of these products do we have? "))
        while newproductstock <= 0 or newproductstock > 100:
            print("Invalid range, try again.")
            newproductstock = int(input("How many of these products do we have? "))
        inventory[newproductname] = [newproductcost, newproductstock]
        print("Product added!")
# If the option is r then the user can delete a product in the inventory and if it
# exists then it will be removed
    if option == "r":
        removeproduct = input("Enter a product name: ")
        if removeproduct in inventory:
            del inventory[removeproduct]
            print("Product removed")
        else:
            print("Unknown product name")
# If the option is u then the user can choose a product that exists in the inventory
# and update any of the three categories, the name, price, or quantity
    if option == "u":
        updateproduct = input("Enter a product name: ")
        if updateproduct in inventory:
            print("What would you like to update?")
            update = input("(n)ame, (p)rice or (q)uantity: ")
            if update == "n":
                updatedname = input("Enter a new name: ")
                while updatedname in inventory:
                    print("Duplicate name!")
                    updatedname = input("Enter a new name: ")
                originalinfo = inventory.get(updateproduct)
                del inventory[updateproduct]
                inventory[updatedname] = originalinfo
                print("Product name has been updated")
            elif update == "p":
                updatedcost = float(input("Enter a new price: "))
                while updatedcost <= 0:
                    print("Invalid price!")
                    updatedcost = float(input("Enter a new cost: "))
                inventory[updateproduct][0] = updatedcost
                print("Product price has been updated")
            elif update == "q":
                updatedstock = int(input("Enter a new quantity: "))
                while updatedstock <= 0:
                    print("Invalid quantity: ")
                    updatedstock = int(input("Enter a new quantity: "))
                inventory[updateproduct][1] = updatedstock
                print("Product quantity has been updated")
            else:
                print("Invalid option", end="\n\n")
        else:
            print("Product doesn't exist. Can't update.")
# If the option is e then based on the inventory, the program will print the most
# expensive item and the least expensive item along with it's price, and it will also
# print the total vlaue of all the items in the inventory
    if option == "e":
        totalvalue = 0
        for x in inventory:
            totalvalue += inventory[x][0]*inventory[x][1]
        print("Total value of all items in inventory: ", format(totalvalue, '.2f'))
        mostexpensiveitem = ""
        mostexpensive = 0
        leastexpensiveitem = ""
        leastexpensive = math.inf
        for key, value in inventory.items():
            value = str(value)
            value = value.split(",")
            value = value[0][1:]
            value = float(value)
            if value > mostexpensive:
                mostexpensive = value
                mostexpensiveitem = key
        for key, value in inventory.items():
            value = str(value)
            value = value.split(",")
            value = value[0][1:]
            value = float(value)
            if value < leastexpensive:
                leastexpensive = value
                leastexpensiveitem = key
        print("Highest priced item:", mostexpensive, "is", mostexpensiveitem)
        print("Lowest priced item:", leastexpensive, "is", leastexpensiveitem)
# If the option is q then the loop will break and the program will end
    if option == "q":
        print("See you soon!")
        break
