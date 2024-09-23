TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

def validation(y, z):
    while True:
        if y < 0:
            print("Number cannot be less than 0!")
            y = 0
            search(z)
        else:
            break

def validation2(y, z):
    if z == 1:
        if y == 11 or y == 31:
            pass
        else:
            print("Please choose either 11 or 31")
            y = 0
            search(z)

def run():
    global tariff
    tariff = int(input("Which tariff? 11 or 31: "))
    validation(tariff, 1)
    validation2(tariff, 1)

def run2():
    global daily_use_kWh
    daily_use_kWh = float(input("Enter daily use in kWh: "))
    validation(daily_use_kWh, 2)

def run3():
    global number_billing_days
    number_billing_days = int(input("Enter number of billing days: "))
    validation(number_billing_days, 3)

def search(z):
    if z == 1:
        run()
    elif z == 2:
        run2()
    elif z == 3:
        run3()

run()
run2()
run3()

if tariff == 11:
    total = TARIFF_11 * daily_use_kWh * number_billing_days
elif tariff == 31:
    total = TARIFF_31 * daily_use_kWh * number_billing_days

print("Estimated bill: $","%.2f" % total)