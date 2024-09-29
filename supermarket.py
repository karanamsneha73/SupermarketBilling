from datetime import datetime
from fractions import Fraction

name = input("Enter your name: ")

items = {
    'rice': {'price': 20, 'unit': 'kg'},
    'sugar': {'price': 30, 'unit': 'kg'},
    'atta powder': {'price': 40, 'unit': 'kg'},
    'oil': {'price': 120, 'unit': 'kg'},
    'soaps': {'price': 15, 'unit': 'units'},
    'chocolates': {'price': 10, 'unit': 'units'}
}

print("Here is the price list:")
for item, details in items.items():
    print(f"{item} - Rs {details['price']} per {details['unit']}")

pricelist = []
total_price = 0

while True:
    option = int(input("Enter 1 to buy items or 2 to exit: "))
    
    if option == 2:
        break
    elif option == 1:
        while True:
            item = input("Enter the item you want to buy (or type 'done' to finish): ").lower()
            if item == 'done':
                break
            elif item in items:
                unit_type = items[item]['unit']
                
                if unit_type == 'kg':
                    quantity_input = input(f"Enter the quantity of {item} in {unit_type} (e.g., 1, 0.5, 1/2): ")
                    try:
                        quantity = float(Fraction(quantity_input))
                    except ValueError:
                        print("Invalid input. Please enter a valid number or fraction (e.g., 1, 0.5, 1/2).")
                        continue
                else:
                    quantity_input = input(f"Enter the quantity of {item} in {unit_type} (e.g., 1, 2, 3): ")
                    try:
                        quantity = int(quantity_input)
                    except ValueError:
                        print("Invalid input. Please enter a whole number (e.g., 1, 2, 3).")
                        continue
                
                price = quantity * items[item]['price']
                pricelist.append((item, quantity, price, unit_type))
                total_price += price
            else:
                print("Sorry, that item is not available.")
    else:
        print("Invalid option.")

if pricelist:
    print("\n----------------- Invoice -----------------")
    print("Date: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Customer Name:", name)
    print("-------------------------------------------")
    print("Item\t\tQuantity\tUnit Price\tTotal Price")
    print("-------------------------------------------")
    for item, quantity, price, unit in pricelist:
        print(f"{item}\t\t{quantity} {unit}\tRs {items[item]['price']}/{unit}\t\tRs {price}")
    print("-------------------------------------------")
    print(f"Total Price: \t\t\t\tRs {total_price}")
    gst = total_price * 5 / 100
    final_price = total_price + gst
    print(f"GST (5%): \t\t\t\tRs {gst}")
    print(f"Final Price (incl. GST): \tRs {final_price}")
    print("-------------------------------------------")

print("Thank you for shopping with us!")

    