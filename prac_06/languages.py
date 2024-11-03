from programming_language import ProgrammingLanguage


python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
list_of_languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for languages in list_of_languages:
    if languages.is_dynamic():
        print(languages.is_dynamic())