#Make a menu to manage a shop from random import choice
menu={'Popcorn': 120, 'Nachos': 180, 'Soda': 30, 'Hot dog': 110, 'Candy': 80}
orders={}
total=0
print("Welcome to the shop, Here's our menu: ")
for key,value in menu.items():
    print(f"{key}: Rs.{value}")
print("Sorry but duel order is not a function, Please order mindfully")
while True:
    choice=input("\nPlease enter a item you want to buy(E to end): ").capitalize()
    if choice=='E':
        break
    while choice not in menu:
        choice = input("\nPlease enter a valid item (e to end): ").capitalize()
    quantity=int(input("Please enter the Quantity you want to purchase: "))
    while quantity<=0:
        quantity=int(input("Please enter a valid quantity: "))
    orders.update({choice:quantity})

print("You have ordered: ")
# print(orders)
for order,quant in orders.items():
    print(f"{order}: X{quant}")
    total+=menu[order]*quant
print(f"Your total is: Rs. {total}")