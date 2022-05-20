import enum

from traitlets import Bool


class Characteristics:
    def __init__(self, age, male, interests):
        self.age = age
        self.male = male
        self.interests = interests

class Person:
    def __init__(self, name, own, other):
        self.name = name
        self.own = own
        self.other = other

people = [
    Person(
        "Bob",
        own=Characteristics(30, male=True, interests=["golf", "walks", "tea"]), 
        other=Characteristics(24, male=False, interests=["tea", "makeup", "food"]), 
    ),
    Person(
        "Mary",
        own=Characteristics(26, male=False, interests=["tea", "knitting", "karate"]), 
        other=Characteristics(32, male=True, interests=["walks", "golf", "trucks"]), 
    ),
]

def match(person, partner) -> Bool:
    return \
        person.own.male == partner.other.male \
        and abs(person.own.age - partner.other.age) <= 5 \
        and any(item in person.own.interests for item in partner.other.interests)


for person in people:
    print(person.name, ":")
    for partner in people:
        if (partner != person):
            if match(person, partner):
                print("Found: ", partner.name)
