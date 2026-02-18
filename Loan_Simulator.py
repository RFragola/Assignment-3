def simulate_loan(balance, annual_rate, monthly_payment):
    monthly_rate = annual_rate / 100 / 12
    months = 0

    # If payment is too small, loan will never be paid off
    if monthly_payment <= balance * monthly_rate:
        print("Monthly payment is too low to ever pay off the loan.")
        return

    while balance > 0:
        # Add monthly interest
        interest = balance * monthly_rate
        balance += interest

        # Subtract payment
        balance -= monthly_payment

        months += 1

        # Prevent negative final balance
        if balance < 0:
            balance = 0

    print(f"\nLoan paid off in {months} months.")


def main():
    while True:
        try:
            loan_amount = float(input("Enter loan amount: $"))
            if loan_amount <= 0:
                print("Loan amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            interest_rate = float(input("Enter annual interest rate (%): "))
            if interest_rate < 0:
                print("Interest rate cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            monthly_payment = float(input("Enter monthly payment: $"))
            if monthly_payment <= 0:
                print("Payment must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    simulate_loan(loan_amount, interest_rate, monthly_payment)


# Run program
main()
