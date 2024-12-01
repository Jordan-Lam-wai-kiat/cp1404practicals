"""monsters = [["Mike", 340, "blue"], ["James", 14, "green"], ["Randall", 24, "purple"]]
scary_monsters = (monster for monster in monsters if (monster[2] > 14))
print(str(scary_monsters))"""
from random import random, randint

from prac_04.list_exercises import user_input

"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} ({self.age})"
p1 = Person("Jane", 19)
print(p1)
people = [Person("Alexa", 21), Person("Siri", 25)]
for line in people:
    print(line)"""

"""
class Monster:
    def __init__(self, name="mike", number_of_teeth=0, colour="blue"):
            self.name = name
            self.number_of_teeth = number_of_teeth
            self.colour = colour
    def __str__(self):
        return f"{self.name}, {self.number_of_teeth}, {self.colour}"
TEETH_THRESHOLD = 16
def is_scary(monster):

    return monster.number_of_teeth > TEETH_THRESHOLD and monster.colour == "red"

monsters = [
    Monster(name="tommy", number_of_teeth=12, colour="red"),
    Monster(name="roger", number_of_teeth=17, colour="red"),
    Monster(name="kinga", number_of_teeth=18, colour="blue")]

for line in monsters:
    print(line, is_scary(line))"""

class User:
    def __init__(self, name, score, number_of_tacos=5):
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score

def give_taco(taco_user):
    from random import randint
    return taco_user.name, taco_user.number_of_tacos - 1, taco_user.score == randint(1, 10)

users = [User(name="Ben", score=10), User(name="Shamaine", score=10), User(name="Isaiah", score=10)]

for line in