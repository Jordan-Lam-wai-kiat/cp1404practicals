sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        bonus = sales * 0.15
    elif sales < 1000:
        bonus = sales * 0.10
    print("%.2f" % bonus)
    sales = float(input("Enter sales: $"))
    if sales == -1:
        break
