import math

# To get a float from user
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# To get an integer from user
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

while True:
# Menu user can choose from
    print()
    print()
    print("FINANCIAL CALCULATOR OPTIONS: ")
    print("  Bond - to calculate the amount you'll have to pay on a home loan.")
    print("  Investment - to calculate the amount of interest you'll earn on your investment.")
    print()
    choice = input("Enter either “investment” or “bond” from the menu above to proceed: ").lower()
    print()
# Bond calculator
    if choice == "bond":
        P = get_float("  Enter the present value of the house in Rands without symbols or spaces: ")
        rate = get_float("  Enter the annual interest rate without symbols (as a percentage, e.g. 7): ")
        n = get_int("  Enter the number of months you plan to repay the bond: ")
        print()
        i = (rate / 100) / 12
        repayment = (i * P) / (1 - (1 + i) ** (-n))
        print(f"Your monthly repayment is: R{repayment:,.2f}")
        print()

# Investment calculator
    elif choice == "investment":
        P = get_float("  Enter the amount (in Rands) you are depositing without symbols or spaces: ")
        rate = get_float("  Enter the interest rate without symbols (as a percentage, e.g. 8): ")
        r = rate / 100
        t = get_int("  Enter the number of years you plan on investing: ")
        print()

        while True:
# Print investment type definitions
            print()
            print()
            print("  Types of interest to choose from: ")
            print("    Simple interest - earn on your original investment amount.")
            print("    Compound interest - earn interest on your current accumulated amount.")
            print()
            interest = input("  Do you want 'simple' or 'compound' interest (or type 'back' to return to main menu)? ").lower()
            print()
            if interest == "simple":
                A = P * (1 + r * t)
                print()
                print()
                print(f"Simple Interest: After {t} years your investment will be worth R{A:,.2f}")
                print()
            elif interest == "compound":
                A = P * math.pow((1 + r), t)
                print()
                print()
                print(f"Compound Interest: After {t} years your investment will be worth R{A:,.2f}")
                print()
            elif interest == "back":
                print()
                print("Returning back to the main menu...")
                break 

            else:
                print("Invalid interest type. Please enter either 'simple','compound' or 'back'.")

    else:
        print("Invalid selection. Please enter either 'bond' or 'investment'.")