import archetypes
import character_creation
import time
import func

# This function will convert a string into a float if possible. If it is not possible, it will return None
def str_to_float(phr1: str) -> float or None:
    try:
        return float(phr1)
    except ValueError:
        return None

# Start Message
print("--------------------------")
print("Welcome to Text-Based RPG!")
print("--------------------------\n")
time.sleep(.5)

# Initialize Character Parameters
# Prompts the user to choose a name for the character
name  = input("Enter Your Character's Name: \n")

# Prompts the user to choose an archetype
print("\nChoose your archetype: ")
i = 0
archetype_list = []
archetype_dict = {}
for key in archetypes.dict1:
    i += 1
    print("[{}] {}".format(i, key))
    archetype_list.extend([key, i])
    archetype_dict[key] = i
archetype = func.user_input("Enter the name or number associated with the archetype: ", archetype_list)
for key in archetype_dict:
    if str_to_float(archetype) is not None:
        if str_to_float(archetype) == archetype_dict[key]:
            archetype = key
    else:
        if archetype.lower() == key.lower():
            archetype = key
func.prompt1()
character1 = character_creation.Character(name, archetypes.Archetypes(archetype))
print(character1)
