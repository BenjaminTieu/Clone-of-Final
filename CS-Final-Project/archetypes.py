import stor
dict1 = stor.archetype_dict

class Archetypes:
    # This method will initialize the attributes of the object
    def __init__(self, archetype: str):
        self.archetype = archetype
        self.description = dict1[archetype]["Description"]
        self.health = dict1[archetype]["Health"]
        self.strength = dict1[archetype]["Strength"]
        self.dexterity = dict1[archetype]["Dexterity"]
        self.agility = dict1[archetype]["Agility"]

    # This method will return all attributes of the object when the object is printed
    def __repr__(self) -> str:
        return ("Archetype: {} \n\n"
                "Description:\n{} \n\n"
                "Health : {}, Strength: {}, Dexterity: {}, Agility: {}"
                .format(self.archetype, self.description, self.health, self.strength, self.dexterity, self.agility))

    # Accessor Methods
    def get_archetype(self) -> str:
        return self.archetype
    def get_description(self) -> str:
        return self.description
    def get_health(self) -> int:
        return self.health
    def get_strength(self) -> int:
        return self.strength
    def get_dexterity(self) -> int:
        return self.dexterity
    def get_agility(self) -> int:
        return self.agility

    # Mutator Methods
    def set_name(self, archetype: str) -> None:
        self.archetype = archetype
    def set_health(self, health: int) -> None:
        self.health = health
    def set_strength(self, strength: int) -> None:
        self.strength = strength
    def set_dexterity(self, dexterity: int) -> None:
        self.dexterity = dexterity
    def set_agility(self, agility: int) -> None:
        self.agility = agility

