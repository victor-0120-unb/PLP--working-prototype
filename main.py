# Northstar Inventory Checker
# Assignment 1 - The Meridian Pivot

inventory = {
    "laptop": 15,
    "phone": 8,
    "keyboard": 0,
    "mouse": 25
}


def check_stock(product_name):
    """
    Check the inventory status of a product.
    """

    product_name = product_name.strip().lower()

    if product_name in inventory:
        stock = inventory[product_name]

        if stock > 0:
            return f"{product_name} is IN STOCK. Quantity available: {stock}"
        else:
            return f"{product_name} is OUT OF STOCK."

    return f"{product_name} was not found in inventory."


def main():
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("   NORTHSTAR INVENTORY CHECKER")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

    product = input("Enter product name: ")

    result = check_stock(product)

    print("\nResult:")
    print(result)


if __name__ == "__main__":
    main()