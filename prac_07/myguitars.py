from guitar import Guitar


def main():
    list_of_guitars = read_file()
    list_of_guitars.sort()
    for guitar in list_of_guitars:
        print(guitar)

def read_file():
    with open("guitars.csv", "r") as in_file:
        list_of_guitars = []
        for line in in_file:
            line = line.strip().split(",")
            list_of_guitars.append(Guitar(line[0], line[1], line[2]))
        return list_of_guitars

main()