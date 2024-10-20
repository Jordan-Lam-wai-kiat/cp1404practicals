CODE_TO_NAME = {"AIR FORCE BLUE": "#5d8aa8", "ALICE BLUE": "#f0f8ff", "ALIZARIN CRIMSON": "#e32636", "ALMOND": "#efdecd",
                "AMARANTH": "#e52b50", "AMBER": "#ffbf00", "AMERICAN ROSE": "#ff033e", "AMETHYST": "#9966cc", "ANDROID GREEN": "#a4c639", "ANTI-FLASH WHITE": "#f2f3f4"}

for code, name in CODE_TO_NAME.items():
    print(f"{code :<3} is {name:<4}")
color_code = input("Enter short state: ").upper()
while color_code != "":
    try:
        print(color_code, "is", CODE_TO_NAME[color_code])
        color_code = input("Enter short state: ").upper()
    except KeyError:
        print("Invalid color name")
        color_code = input("Enter short state: ").upper()
