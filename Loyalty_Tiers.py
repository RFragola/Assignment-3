def main():
    tier_counts = {
        "Bronze": 0,
        "Silver": 0,
        "Gold": 0
    }

    print("Enter customers (type 0 as name to finish)")

    while True:
        name = input("Enter customer name: ")

        if name == "0":
            break

        # Validate purchase amount
        while True:
            try:
                total = float(input("Enter total purchase amount: $"))
                if total < 0:
                    print("Purchase amount cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        # Determine tier
        if total < 1000:
            tier_counts["Bronze"] += 1
        elif 1000 <= total <= 4999:
            tier_counts["Silver"] += 1
        else:
            tier_counts["Gold"] += 1

        print("Customer recorded!\n")

    print("\n----- Loyalty Tier Summary -----")
    for tier in tier_counts:
        print(f"{tier}: {tier_counts[tier]} customers")


# Run program
main()
