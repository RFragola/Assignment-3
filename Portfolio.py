import random


def calculate_total_value(portfolio):
    total = 0
    for stock in portfolio:
        shares = portfolio[stock]["shares"]
        price = portfolio[stock]["price"]
        total += shares * price
    return total


def simulate_week(portfolio):
    print("\n--- Simulating 1 Week of Price Changes ---")

    for day in range(1, 6):
        print(f"\nDay {day}")

        for stock in portfolio:
            percent_change = random.uniform(-0.05, 0.05)
            old_price = portfolio[stock]["price"]
            new_price = old_price * (1 + percent_change)

            portfolio[stock]["price"] = new_price
            print(f"{stock} new price: ${new_price:.2f}")

        total_value = calculate_total_value(portfolio)
        print(f"Total Portfolio Value: ${total_value:.2f}")


def main():
    portfolio = {}

    print("Enter your stocks (type 0 as the stock symbol to finish)\n")

    while True:
        symbol = input("Enter stock symbol: ").upper()

        if symbol == "0":
            break

        # Shares input validation
        while True:
            try:
                shares = int(input("Enter number of shares: "))
                if shares <= 0:
                    print("Shares must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Please enter a valid whole number.")

        # Price input validation
        while True:
            try:
                price = float(input("Enter price per share: $"))
                if price <= 0:
                    print("Price must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        portfolio[symbol] = {
            "shares": shares,
            "price": price
        }

        print("Stock added!\n")

    if len(portfolio) == 0:
        print("No stocks entered.")
        return

    print("\n--- Your Portfolio ---")
    for stock in portfolio:
        print(f"{stock}: {portfolio[stock]['shares']} shares @ ${portfolio[stock]['price']:.2f}")

    total_value = calculate_total_value(portfolio)
    print(f"\nInitial Total Value: ${total_value:.2f}")

    simulate_week(portfolio)


# Run program
main()
