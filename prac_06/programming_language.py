class ProgrammingLanguage:
    def __init__(self, programming_language, typing, reflection, year):
        self.programming_language = programming_language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.reflection is True:
            return self.programming_language

    def __str__(self):
        return f"{self.programming_language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"