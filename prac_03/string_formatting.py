constant = 2
variable = 0
for i in range(0, 11, 1):
    result = constant ** variable
    print(f"{constant} ^{variable:>2} is {result:>5}")
    variable += 1
