produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]

for section in groceries:
    for i in section:
        print(f"Item name: {i}")
