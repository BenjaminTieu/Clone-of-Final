dict1 = {"Warrior": {"Health": 10, "Strength": 10, "Dexterity": 5, "Agility": 5},
         "Thief": {"Health": 5, "Strength": 5, "Dexterity": 10, "Agility": 10}}

class Archetypes:
    # This method will initialize the attributes of the object
    def __init__(self, archetype: str):
        self.archetype = archetype
        self.health = dict1[archetype]["Health"]
        self.strength = dict1[archetype]["Strength"]
        self.dexterity = dict1[archetype]["Dexterity"]
        self.agility = dict1[archetype]["Agility"]

    # This method will return all attributes of the object when the object is printed
    def __repr__(self) -> str:
        return ("Archetype: {}, Health : {}, Strength: {}, Dexterity: {}, Agility: {}"
                .format(self.archetype, self.health, self.strength, self.dexterity, self.agility))

    # Accessor Methods
    def get_name(self) -> str:
        return self.archetype
    def get_health(self) -> int:
        return self.health
    def get_strength(self) -> int:
        return self.strength
    def get_dexterity(self) -> int:
        return self.dexterity
    def get_agility(self) -> int:
        return self.agility

