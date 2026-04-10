# Each item contains current stock, minimum required stock, and restock quantity
inventory = {
    "Bread": [42, 60, 10],   # "Item": [current stock, minimum stock, restock quantity]
    "Eggs": [225, 200, 40],  # Eggs are sufficiently stocked
    "Apples": [9, 50, 20]    # Apples need restocking
}
while inventory["Bread"][0] < inventory["Bread"][1]:
    print(f"Bread stock is low: {inventory["Bread"][0]} units. Restocking...")
    inventory["Bread"][0] += inventory["Bread"][2]
print(f"Final Inventory after restocing: Bread: {inventory["Bread"][0]} units (Minimum required: {inventory["Bread"][1]} units)")

while inventory["Eggs"][0] < inventory["Eggs"][1]:
    print(f"Eggs stock is low: {inventory["Eggs"][0]} units. Restocking...")
    inventory["Eggs"][0] += inventory["Eggs"][2]
print(f"Final Inventory after restocing: Eggs: {inventory["Eggs"][0]} units (Minimum required: {inventory["Eggs"][1]} units)")

while inventory["Apples"][0] < inventory["Apples"][1]:
    print(f"Apples stock is low: {inventory["Apples"][0]} units. Restocking...")
    inventory["Apples"][0] += inventory["Apples"][2]
print(f"Final Inventory after restocing: Apples: {inventory["Apples"][0]} units (Minimum required: {inventory["Apples"][1]} units)")