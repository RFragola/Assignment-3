def calculate_commission(sales_amount):
    """Returns 10% commission for a given sales amount."""
    return sales_amount * 0.10


def print_leaderboard(sales):
    commissions = {}

    # Calculate commissions using a for loop
    for employee in sales:
        commissions[employee] = calculate_commission(sales[employee])

    # Sort employees by commission (highest first)
    sorted_commissions = sorted(
        commissions.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("----- Commission Leaderboard -----")

    rank = 1
    for employee, commission in sorted_commissions:
        print(f"{rank}. {employee} - Commission: ${commission:.2f}")
        rank += 1


# Given sales data
sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}

print_leaderboard(sales)
