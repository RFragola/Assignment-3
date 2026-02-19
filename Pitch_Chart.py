def main():
    revenues = []

    print("Startup Revenue Visualizer (type number of years)\n")

    # Ask for number of years
    while True:
        try:
            years = int(input("How many years to project? "))
            if years <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number.")

    # Collect revenue data
    for year in range(1, years + 1):
        while True:
            try:
                revenue = float(input(f"Enter projected revenue for Year {year}: "))
                if revenue < 0:
                    print("Revenue cannot be negative.")
                    continue
                revenues.append(revenue)
                break
            except ValueError:
                print("Please enter a valid number.")

    # Find max revenue to scale chart
    max_revenue = max(revenues)

    print("\n----- Startup Pitch Deck Revenue Chart -----")

    # Create ASCII bars
    for i in range(len(revenues)):
        # Scale bars to max 40 hashes
        bar_length = int((revenues[i] / max_revenue) * 40)
        bar = "#" * bar_length

        print(f"Year {i+1}: {bar}")
