class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def writeline(self):
        """returns guitar tuple"""
        guitar = (self.name, self.year, self.cost)
        return guitar


    def get_age(self):
        """returns difference in age"""
        age = 2024 - self.year
        return age

    def is_vintage(self):
        """checks object is vintage by checking if age is more than 50 years old"""
        age = self.get_age()
        if age > 50:
            return "(vintage)"
        else:
            return ""

    def get_name(self):
        """request for user to input name"""
        user_input = input("Name: ")
        self.name = user_input

    def get_year(self):
        """request for user to input year of guitar creation"""
        year = int(input("Year: "))
        self.year = year

    def get_cost(self):
        """request for user to enter price of guitar"""
        cost = int(input("Cost: $"))
        self.cost = cost