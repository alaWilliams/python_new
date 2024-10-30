#Shopping cart
item = input('Enter the item you want to buy?: ')
price = float(input('How much does it cost? '))
quantity = int(input('How many would you like to buy? '))
total = price * quantity

print(f'You have bought {quantity} x {item}\nYou total is ${total}')