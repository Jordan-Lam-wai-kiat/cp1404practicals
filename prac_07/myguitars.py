from guitar import Guitar

def main():
    """sorts and orders guitar details by ascending order with reference to cost """
    list_of_guitars = read_file()
    list_of_guitars.sort()
    list_of_guitars_to_save = []
    for guitar in list_of_guitars:
        print(guitar)
    guitar = Guitar()
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
            with open("guitars.csv", "a") as out_file:
                out_file.write(f"\n{guitar.name},{guitar.year},{guitar.cost:.2f}")
            list_of_guitars.append(Guitar(guitar.name, guitar.year, guitar.cost))


def read_file():
    """reads guitar.csv and displays the data into a readable format"""
    with open("guitars.csv", "r") as in_file:
        list_of_guitars = []
        for line in in_file:
            line = line.strip().split(",")
            list_of_guitars.append(Guitar(line[0], line[1], line[2]))
        return list_of_guitars




main()