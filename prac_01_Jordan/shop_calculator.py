while True:
    num_of_items = int(input("Number of items: "))
    if num_of_items < 0:
        print("Invalid number of items!")
    else:
        break
total = 0
for i in range(1, num_of_items + 1):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total = total * 0.90

print('Total Price for all', num_of_items, 'items is $',"%.2f" % total)
