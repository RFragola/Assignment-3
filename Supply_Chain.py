def calculate_total_inventory(warehouses):
    total_inventory = {}

    # Outer loop → each warehouse
    for warehouse in warehouses:
        inventory = warehouse["inventory"]

        # Inner loop → each product
        for product in inventory:
            quantity = inventory[product]

            if product in total_inventory:
                total_inventory[product] += quantity
            else:
                total_inventory[product] = quantity

    return total_inventory


def main():
    warehouses = []

    print("Enter warehouse data (type 0 to stop)\n")

    while True:
        name = input("Enter warehouse name: ")

        if name == "0":
            break

        inventory = {}

        print(f"\nEntering inventory for {name} (type 0 to stop products)")

        while True:
            product = input("Enter product name: ").title()

            if product == "0":
                break

            while True:
                try:
                    quantity = int(input(f"Enter quantity of {product}: "))
                    if quantity < 0:
                        print("Quantity cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid whole number.")

            inventory[product] = quantity

        warehouses.append({
            "name": name,
            "inventory": inventory
        })

        print(f"{name} added!\n")

    if len(warehouses) == 0:
        print("No warehouses entered.")
        return

    totals = calculate_total_inventory(warehouses)

    print("\n----- Supply Chain Total Inventory -----")
    for product in totals:
        print(f"{product}: {totals[product]} units")


# Run program
main()
