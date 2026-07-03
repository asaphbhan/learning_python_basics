#Shopping cart
print("This is a shopping cart program")
items=[]
prices=[]
total=0
food='a'
while True:
    food=input("Please enter the food item you want to buy(enter q to get you total):")
    if food=='Q':
       food.lower()
    elif food=='q':
        break
    pri=int(input("Please enter it's price"))
    while pri<=0 :
        pri=int(input("Please enter valid price: Rs."))
    items.append(food)
    prices.append(pri)

for price in prices:
    total+=price

print("The items in your list are: ")
for item in items:
    print(item)
print(f"Your total comes out to be: Rs.{total:8.2f}")
