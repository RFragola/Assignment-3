def expense_summary():
    expenses = {
        "Travel": [],
        "Meals": [],
        "Supplies": []
    }

    print("---- Employee Expense Entry ----")

    # Ask for expenses by category
    for category in expenses:
        print(f"\nEntering expenses for {category}")
        
        while True:  #loop to go through all 3
            try:
                amount = float(input(f"Enter {category} expense (0 to continue): $"))
                
                if amount == 0:
                    break
                
                if amount < 0:
                    print("Expense cannot be negative. Try again.")
                    continue
                
                expenses[category].append(amount)
            
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Print report
    grand_total = 0
    print("\n----- Expense Summary Report -----")

    for category in expenses:
        category_total = 0
        
        for amount in expenses[category]:
            category_total += amount
        
        grand_total += category_total
        print(f"{category} Total: ${category_total:.2f}")

    print("----------------------------------")
    print(f"Grand Total: ${grand_total:.2f}")


expense_summary()
