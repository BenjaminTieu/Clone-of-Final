import archetypes

class Character:
    # This method will initialize the attributes of the object
    def __init__(self, name: str, archetype: archetypes.Archetypes):
        self.name = name
        self.health = archetype.health
        self.strength = archetype.strength
        self.dexterity = archetype.dexterity
        self.agility = archetype.agility
        self.archetype = archetype

    # This method will return all attributes of the object when the object is printed
    def __repr__(self) -> str:
        return ("Name: {}, Archetype: {}, Health : {}, Strength: {}, Dexterity: {}, Agility: {}"
                .format(self.name, self.archetype.get_archetype(), self.health,self.strength, self.dexterity,
                        self. agility,))

    # Accessor methods
    def get_name(self) -> str:
        return self.name
    def get_health(self) -> int:
        return self.health
    def get_strength(self) -> int:
        return self.strength
    def get_dexterity(self) -> int:
        return self.dexterity
    def get_agility(self) -> int:
        return self.agility
    def get_archetype(self) -> str:
        return self.archetype.get_archetype()

    # Mutator Methods
    def set_name(self, name: str) -> None:
        self.name = name
    def set_health(self, health: int) -> None:
        self.health = health
    def set_strength(self, strength: int) -> None:
        self.strength = strength
    def set_dexterity(self, dexterity: int) -> None:
        self.dexterity = dexterity
    def set_agility(self, agility: int) -> None:
        self.agility = agility
    def set_archetype(self, archetype: int) -> None:
        self.archetype = archetype
