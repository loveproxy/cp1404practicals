
# define the number of items
num_items = int(input("Number of items: "))
if num_items < 0:
    print("Invalid number of items!")
total_price = 0.0

# sum the total price of the items
for i in range(num_items):
    price = float(input(f"Price of item: "))
    if price < 0:
        print("Invalid price! Price cannot be negative.")
    else:
        total_price += price
        print(f"Total price for {num_items} items is ${total_price:.2f}")

# decide whether to give discount
if total_price > 100:
    discount = total_price * 0.10
    total_price -= discount
    print(f"Total price for {num_items} items is ${total_price:.2f}")
