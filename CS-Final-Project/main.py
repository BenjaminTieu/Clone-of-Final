import archetypes
import character_creation

# This function will convert a string into a float if possible. If it is not possible, it will return None
def str_to_float(phr1: str) -> float or None:
    try:
        return float(phr1)
    except ValueError:
        return None

# This function will ask the user for an input. If the input is not an expected value, then the user will be re-prompted
def user_input(phr1:str, accepted_choices: list):
    check = False
    # This while loop will force the program to run until it gets an expected value
    while check is False:
        val = str(input(phr1 + "\n"))
        for val2 in accepted_choices:
            # Check if the input is a string or number
            check_string = True
            contains_string = False
            for char in val:
                if char.isdigit():
                    check_string = False
                else:
                    contains_string = True
            # Check for a leading zero
            if len(val) > 1 and check_string is False and contains_string is False and float(val[0]) == 0:
                check_string = True
            # Check if the input is a valid number
            if check_string is False and contains_string is False:
                if float(val) == val2:
                    print("\n", end = "")
                    return float(val)
            # Check if the input is a valid String (Capitalization is inconsequential)
            elif check_string and isinstance(val2, str):
                if val.upper().strip() == val2.upper().strip():
                    print("\n", end = "")
                    return val2
        print("Error. You have entered an invalid option.")

# Start Message
print("--------------------------")
print("Welcome to Text-Based RPG!")
print("--------------------------\n")

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
archetype = user_input("Enter the name or number associated with the archetype: ", archetype_list)
for key in archetype_dict:
    if str_to_float(archetype) is not None:
        if str_to_float(archetype) == archetype_dict[key]:
            archetype = key
    else:
        if archetype.lower() == key.lower():
            archetype = key

character1 = character_creation.Character(name, archetypes.Archetypes(archetype))
print(character1)
