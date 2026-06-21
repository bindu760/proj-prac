print(input("Enter your name: "))
products = {
    "Mouse": {"price": 1200, "stock": 50},
    "Keyboard": {"price": 2500, "stock": 20},
    "Laptop": {"price": 70000, "stock": 15}
}

#show all the products
print("Available Products:")
for name, details in products.items():
    print(f"{name} - Price: Rs.{details['price']} - Stock: {details['stock']}")

#1 sale of Mouse
products["Mouse"]["stock"] -= 1

print("\nAfter Sale:")
print("Mouse Stock =", products["Mouse"]["stock"])
