# ==========================================
#       STOCK MARKET PROFIT/LOSS ANALYSIS
# ==========================================

print("==========================================")
print("        STOCK MARKET ANALYSIS")
print("==========================================")

print("\nSelect the time period:")
print("1. 1 Week")
print("2. 1 Month")
print("3. 6 Months")
print("4. 1 Year")
print("5. 3 Years")
print("6. 5 Years")

choice = int(input("\nEnter your choice: "))

# Periods
periods = {
    1: ("1 Week", 7, "Day"),
    2: ("1 Month", 30, "Day"),
    3: ("6 Months", 6, "Month"),
    4: ("1 Year", 12, "Month"),
    5: ("3 Years", 36, "Month"),
    6: ("5 Years", 60, "Month")
}

if choice not in periods:
    print("Invalid choice!")

else:
    period_name, default_count, unit = periods[choice]

    print("\nYou selected:", period_name)

    # Allow user to decide number of periods
    count = int(input(
        f"How many {unit.lower()}s do you want to enter? "
    ))

    opening_prices = []
    closing_prices = []

    # ------------------------------------------
    # Take opening and closing prices
    # ------------------------------------------

    for i in range(1, count + 1):

        print(f"\n{unit} {i}")

        opening = float(
            input("Enter Opening Price: ₹")
        )

        closing = float(
            input("Enter Closing Price: ₹")
        )

        opening_prices.append(opening)
        closing_prices.append(closing)

    # ------------------------------------------
    # Display individual results
    # ------------------------------------------

    print("\n==========================================")
    print("           ANALYSIS RESULTS")
    print("==========================================")

    for i in range(count):

        profit_loss = closing_prices[i] - opening_prices[i]

        if profit_loss > 0:
            status = "PROFIT"
        elif profit_loss < 0:
            status = "LOSS"
        else:
            status = "NO PROFIT / NO LOSS"

        print(f"\n{unit} {i + 1}")
        print("Opening Price :", "₹", opening_prices[i])
        print("Closing Price :", "₹", closing_prices[i])
        print("Change        :", "₹", round(profit_loss, 2))
        print("Status        :", status)

    # ------------------------------------------
    # Overall analysis
    # ------------------------------------------

    first_opening = opening_prices[0]
    last_closing = closing_prices[-1]

    overall_change = last_closing - first_opening
    overall_percentage = (overall_change / first_opening) * 100

    print("\n==========================================")
    print("            OVERALL RESULT")
    print("==========================================")

    print("First Opening Price :", "₹", first_opening)
    print("Last Closing Price  :", "₹", last_closing)

    if overall_change > 0:
        print("Overall Status      : PROFIT")
        print("Total Profit        :", "₹", round(overall_change, 2))
        print("Profit Percentage   :", round(overall_percentage, 2), "%")

    elif overall_change < 0:
        print("Overall Status      : LOSS")
        print("Total Loss          :", "₹", round(abs(overall_change), 2))
        print("Loss Percentage     :", round(abs(overall_percentage), 2), "%")

    else:
        print("Overall Status      : NO PROFIT / NO LOSS")
        print("Change              : ₹ 0")