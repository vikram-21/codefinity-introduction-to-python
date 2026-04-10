# List representing the current stock of items
stock_items = [
    ["Apples", 30],
    ["Bananas", 20],
    ["Oranges", 15],
    ["Tomatoes", 25]
]

# Quantities received from the new shipment
shipment_received = [["Apples", 120], ["Bananas", 180], ["Oranges", 100], ["Tomatoes", 150]]

prices = [29.99, 45.50, 12.75, 38.20]

discount_factor = [0.10, 0.20, 0.15, 0.05]

for cost in range(len(prices)):
    prices[cost] -= prices[cost]*discount_factor[cost]
    print(f"Updated price for item {cost}: ${prices[cost]:.2f}")
