# Define class of characterics that described both a person amd what they desire in a match  - consising of age, gender and interests.
class Characteristics:
    def __init__(self, age, male, interests):
        self.age = age
        self.male = male
        self.interests = interests

# Define  class for a person, identifying them by name, their characterictics ("own") and the characteristics they desire in their match ("desired").
class Person:
    def __init__(self, name, own, desired):
        self.name = name
        self.own = own
        self.desired = desired

# Define the list of people participating in "matchmaking" (the cast of Friends was used as an example)
people = [
    Person(
        name="Joey",
        own=Characteristics(25, male=True, interests=["dating", "sports", "music"]), 
        desired=Characteristics(20, male=False, interests=["music", "animals", "cooking"]),
    ),
    Person(
        "Phoebe",
        own=Characteristics(27, male=False, interests=["music", "civil disobedience", "animals"]), 
        desired=Characteristics(35, male=True, interests=["sports", "music", "animals"]), 
    ),
      Person(
        "Chandler",
        own=Characteristics(25, male=True, interests=["TV", "humour", "animals"]), 
        desired=Characteristics(24, male=False, interests=["coffee", "cooking", "cleaning"]), 
    ),
    Person(
        "Monica",
        own=Characteristics(24, male=False, interests=["coffee", "cooking", "cleaning"]), 
        desired=Characteristics(25, male=True, interests=["TV", "humour", "animals"]), 
    ), 
    Person(
        "Ross",
        own=Characteristics(26, male=True, interests=["getting married", "paleontology", "karate"]), 
        desired=Characteristics(28, male=False, interests=["science", "reading", "animals"]), 
    ),
    Person(
        "Rachel",
        own=Characteristics(24, male=False, interests=["coffee", "fashion", "shopping"]), 
        desired=Characteristics(33, male=None, interests=["humour", "shopping", "arts"]), 
    ),
]
# Calculate match score.
# Higher score means "partner" better match for "person".
def score(person, partner):
    return \
        (1 if partner.own.male == person.desired.male or person.desired.male == None else 0) * \
        (len(set(partner.own.interests).intersection(set(person.desired.interests))) \
        + (1 / (abs(partner.own.age - person.desired.age) + 1)))


# Create "for_ loop" for each person and nested "for_loop" to calculate score with every other person.
for person in people:
    print(person.name, ":")
    best_score = 0
    best_partner = None
    for partner in people:
        if (partner != person):
            person_matches_partner = score(person, partner)
            partner_matches_person = score(partner, person)
            combined_score = partner_matches_person + person_matches_partner
            print(person.name, "matches", partner.name, person_matches_partner)
            print(partner.name, "matches", person.name, partner_matches_person)
            print(partner.name, "and", person.name, combined_score)
            if combined_score > best_score:
                best_score = combined_score
                best_partner = partner
    print()
    print("Best match for", person.name, ":", best_partner.name, "Score:", best_score)
    print()
