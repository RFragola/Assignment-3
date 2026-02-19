def main():
    # Get initial revenue
    while True:
        try:
            revenue = float(input("Enter initial revenue: $"))
            if revenue <= 0:
                print("Revenue must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Get growth rate
    while True:
        try:
            growth_rate = float(input("Enter annual growth rate (%): "))
            break
        except ValueError:
            print("Please enter a valid number.")

    growth_rate = growth_rate / 100  # Convert percent to decimal

    print("\n----- 10-Year Revenue Projection -----")
    print("Year\tProjected Revenue")
    print("-------------------------------------")

    # Project revenue for 10 years
    for year in range(1, 11):
        revenue = revenue * (1 + growth_rate)
        print(f"{year}\t${revenue:,.2f}")


# Run program
main()
