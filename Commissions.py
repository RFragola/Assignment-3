def calculate_commission(sales_amount):
    return sales_amount * 0.10


def print_leaderboard(sales):
    commissions = {}

    # Calculate commissions
    for employee in sales:
        commissions[employee] = calculate_commission(sales[employee])

    # Sort by commission (highest first)
    sorted_commissions = sorted(
        commissions.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\n----- Commission Leaderboard -----")

    rank = 1
    for employee, commission in sorted_commissions:
        print(f"{rank}. {employee} - Commission: ${commission:.2f}")
        rank += 1


def main():
    sales = {}

    try:
        num_employees = int(input("How many employees? "))
    except ValueError:
        print("Invalid number. Exiting program.")
        return

    for i in range(num_employees):
        print(f"\nEmployee {i + 1}")
        name = input("Enter employee name: ")

        while True:
            try:
                amount = float(input("Enter total sales: $"))
                if amount < 0:
                    print("Sales cannot be negative. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        sales[name] = amount

    print_leaderboard(sales)


# Run the program
main()
