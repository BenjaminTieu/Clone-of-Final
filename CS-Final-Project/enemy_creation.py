class Enemy:
    # This method will initialize the attributes of the object
    def __init__(self, name: str, hp: int, strength: int, dex: int, agl: int):
        self.name = name
        self.health = hp
        self.strength = strength
        self.dexterity = dex
        self.agility = agl

    # This method will return all attributes of the object when the object is printed
    def __repr__(self) -> str:
        return ("Name: {}, Health : {}, Strength: {}, Dexterity: {}, Agility: {}"
                .format(self.name, self.health, self.strength,self.dexterity, self.agility))

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