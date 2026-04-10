# Each product has a list with current stock as the first item 
# and minimum stock as the second item
inventory = {
    "Milk": [25, 20],
    "Eggs": [250, 200],
    "Bread": [30, 50],  # This item needs restocking
    "Apples": [50, 45]
}

# Promotions dictionary
promotions = {
    "Eggs": "20% off",
    "Apples": "Buy one, get one free"
}

for product in inventory:
    print(f"--- Processing:{product} ---")
    if inventory[product][0] <= inventory[product][1]:
        print(f"{product} needs restocking. Current stock: {inventory[product][0]}. Minimum required: {inventory[product][1]}")
        inventory[product][0] += 20
        print(f"Updated stock for {product}: {inventory[product][0]}")
    if product in promotions:
        print(f"Promotion for {product}: {promotions[product]}")
    else:
        print("No promotions for ", product)
        