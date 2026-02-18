def market_share_summary():
    # Sample survey data
    preferences = ["coffee", "tea", "coffee", "soda", "soda", "tea", "coffee", "soda", "juice", "coffee", "coffee", "tea", "coffee"]

    counts = {}  # Dictionary to store counts

    # Count each preference
    for item in preferences:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    total_responses = len(preferences)

    print("--- Market Share Summary ---")

    # Calculate and print percentages
    for product in counts:
        percentage = (counts[product] / total_responses) * 100
        print(f"{product}: {percentage:.0f}%")

# Run the program
market_share_summary()
