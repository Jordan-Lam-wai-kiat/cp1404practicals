from guitar import Guitar

guitar = Guitar()
guitars = []

longest_name = 0
highest_cost = 0
end = False
while end == False:
    name = guitar.get_name()
    if str(guitar.name) == "":
        end = True
    if len(str(guitar.name)) > longest_name:
        longest_name = len(str(guitar.name))
    if end == False:
        cost = guitar.get_cost()
        if len(str(guitar.cost)) > highest_cost:
            highest_cost = len(str(guitar.cost))
        year = guitar.get_year()
        guitars.append(Guitar(guitar.name, guitar.year, guitar.cost))
    else:
        print(f"\n... snip ...")

count = 0
print("These are my guitars:")
for guitar in guitars:
    count += 1
    is_vintage = guitar.is_vintage()
    print(f"Guitar {count}:  {guitar.name :{longest_name}} ({guitar.year}), worth $ {guitar.cost :{highest_cost}} {is_vintage}")