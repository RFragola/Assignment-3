def retail_checkout():
    prices = []  # List to store item prices

    while True:
        try:
            price = float(input("Enter item price (enter 0 to end): $"))

            # Exit condition
            if price == 0:
                break

            # Input validation (no negative prices)
            if price < 0:
                print("Price cannot be negative. Please try again.")
                continue

            prices.append(price)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Calculations
    if len(prices) > 0:
        total = sum(prices)
        average = total / len(prices)
        count = len(prices)

        print("\n--- Purchase Summary ---")
        print(f"Total purchase amount: ${total:.2f}")
        print(f"Average item cost: ${average:.2f}")
        print(f"Number of items bought: {count}")
    else:
        print("\nNo items were purchased.")


# Run the program
retail_checkout()