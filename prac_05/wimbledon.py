filename = "wimbledon.csv"
with open(filename, "r", encoding="utf-8-sig") as in_file:
    list_of_values = in_file.readlines()
    print(list_of_values)
    for line in list_of_values:
        line.split(",")
    print(list_of_values)
    list_of_scores = list_of_values[1:][5]
    print(list_of_scores)
