import archetypes
import character_creation
import time
import func

# Start Message
print("--------------------------")
print("Welcome to Text-Based RPG!")
print("--------------------------\n")
time.sleep(.5)

# Initialize Character Parameters
# Prompts the user to choose a name for the character
name  = input("Enter Your Character's Name: \n")
# Confirmation for name
print("\n", end="")
func.user_input("Are you sure you want to name your character {}?".format(name), ["yes", "no"])

# Prompts the user to choose an archetype
archetype = func.user_input("Choose your archetype", ["Warrior", "Thief"])
func.prompt1()
character1 = character_creation.Character(name, archetypes.Archetypes(archetype))
print(character1)
