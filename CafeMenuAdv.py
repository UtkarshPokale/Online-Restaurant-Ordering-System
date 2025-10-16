# Online Restaurant Ordering System

menu = {
    'Pizza': 120,
    'Pasta': 100,
    'Burger': 80,
    'Salad': 70,
    'Coffee': 60,
    'Sandwich': 90,
    'Fries': 50,
    'Momos': 110,
    'Cold Drink': 40,
    'Ice Cream': 60
}

print("🍽️ Welcome to the Online Restaurant 🍽️")
print("\n-------- MENU CARD --------")
for item, price in menu.items():
    print(f"{item}: Rs {price}")
print("---------------------------\n")

order_total = 0
ordered_items = []

while True:
    item = input("Enter the name of the item you want to order (or type 'quit' to finish): ").title()
    
    if item.lower() == 'quit':
        break

    if item in menu:
        quantity = int(input(f"Enter quantity for {item}: "))
        total_price = menu[item] * quantity
        order_total += total_price
        ordered_items.append((item, quantity, total_price))
        print(f"✅ {quantity} x {item} added to your order. Subtotal: Rs {total_price}\n")
    else:
        print(f"❌ Sorry, {item} is not available in our menu.\n")

# Print final bill
print("\n--------- BILL SUMMARY ---------")
for item, qty, price in ordered_items:
    print(f"{item} x {qty} = Rs {price}")
print("--------------------------------")
print(f"Total amount to pay: Rs {order_total}")
print("🙏 Thank you for ordering with us! Visit again 😊")
