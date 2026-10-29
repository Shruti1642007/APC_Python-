# Inventory Management System

inventory = {}

# Function to add a product
def add_product(name, quantity):
    inventory[name] = quantity
    print("Product added successfully.")


# Function to update product quantity
def update_product(name, quantity):
    if name in inventory:
        inventory[name] = quantity
        print("Quantity updated successfully.")
    else:
        print("Product not found.")


# Function to remove a product
def remove_product(name):
    if name in inventory:
        del inventory[name]
        print("Product removed successfully.")
    else:
        print("Product not found.")


# Function to display product with highest stock
def highest_stock():
    if inventory:
        product = max(inventory, key=inventory.get)
        print("Highest stock product:", product)
        print("Quantity:", inventory[product])
    else:
        print("Inventory is empty.")


# Function to display total unique products
def total_products():
    print("Total unique products:", len(inventory))


# Add products
add_product("Pen", 50)
add_product("Book", 30)
add_product("Bag", 20)
add_product("Pencil", 40)

# Update quantity
update_product("Book", 45)

# Display highest stock
highest_stock()

# Remove a product when quantity reaches 0
update_product("Bag", 0)

if inventory.get("Bag") == 0:
    remove_product("Bag")

# Display total products
total_products()

# Display final inventory
print("\nFinal Inventory:")
print(inventory)