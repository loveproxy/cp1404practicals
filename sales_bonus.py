#CP1404/CP5632 - Practical
sales = float(input("Enter sales: $"))
bonus_rate_low = 0.1
bonus_rate_high = 0.15
while sales >= 0:
    if sales < 1000:
        bonus = sales * bonus_rate_low
        print(f"Get bonus:$",bonus)
        # break
    else:
        bonus = sales * bonus_rate_high
        print(f"Get bonus:$",bonus)
        # break
    sales = float(input("Enter sales: $"))

