name = input("Enter your name: ")
print("Welcome", name)

products = {
    "Mouse": {"price": 1200, "stock": 50},
    "Keyboard": {"price": 2500, "stock": 20},
    "Laptop": {"price": 70000, "stock": 15}
}

print("Available Products:")
for product, details in products.items():
    print(f"{product} - Price: Rs.{details['price']} - Stock: {details['stock']}")

# input
product_name = input("Enter product name you want to buy: ").strip().capitalize()#strip() removes leading and trailing whitespace, capitalize() makes the first letter uppercase and the rest lowercase

# check first (MOST IMPORTANT)
if product_name in products:
    quantity = int(input("Enter quantity: "))

    if quantity <= products[product_name]["stock"]:
        total_price = products[product_name]["price"] * quantity
        print(f"Total price: Rs.{total_price}")

        products[product_name]["stock"] -= quantity
    else:
        print(f"Sorry, only {products[product_name]['stock']} {product_name} are available.")
else:
    print("❌ Product not available in our store.")