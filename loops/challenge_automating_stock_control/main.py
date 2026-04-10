# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print(f"Processing started")
for each in inventory:
    print(f"Processing {each}")
    current_stock, min_stock, restock_amount, on_sale = inventory[each]
    while current_stock < min_stock:
        current_stock += restock_amount
    inventory[each][0] = current_stock
    if current_stock > discount_threshold and not on_sale:
        inventory[each][3] = True

print(f"Processing completed")
    