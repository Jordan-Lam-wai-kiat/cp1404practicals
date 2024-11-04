class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year



    def get_age(self):
        age = 2024 - self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        if age > 50:
            return "(vintage)"
        else:
            return ""

    def get_name(self):
        user_input = input("Name: ")
        self.name = user_input

    def get_year(self):
        year = int(input("Year: "))
        self.year = year

    def get_cost(self):
        cost = int(input("Cost: $"))
        self.cost = cost