
print("Electricity bill estimator")

# Get user inputs
cents_per_kwh = float(input("Enter cents per kWh: "))
daily_use_kwh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

# Calculate the total bill in dollars
total_bill = (cents_per_kwh * daily_use_kwh * billing_days) / 100


tax_rate = int(input("Which tariff? 11 or 31:"))
# constant
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
if tax_rate == 11:
    total_bill = total_bill*(1 + TARIFF_11)
elif tax_rate == 31:
    total_bill = total_bill * (1 + TARIFF_31)

# Display the estimated bill
print(f"Estimated bill: ${total_bill:.2f}")
