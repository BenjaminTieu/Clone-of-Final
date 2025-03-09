import stor

# This function will ask the user for an input. If the input is not an expected value, then the user
#   will be re-prompted.
# Note that, by design, this function will see any leading zeroes (if the user inputs an integer),
#   capitalization mismatches, and leading/trailing spaces as an expected value if the rest of the
#   input matches a value from the list of accepted choices.
# Usage of all arguments:
#       phr1: A string that holds the question that prompts the user for an input
#       accepted_choices: an OPTIONAL list of string objects that stores the acceptable choices
#                           a user can input
#       confirmation: an OPTIONAL boolean that is only used to check if a confirmation statement
#                       is being printed to the screen. The acceptable choices should be either
#                       yes or no if confirmation is set to True.
# This function will normally return the valid choice (if a number is associated with the choice,
#   it will return the choice not the number). However, if the argument passed to the third
#   parameter is True, this function will return a boolean value.
def user_input(phr1:str, accepted_choices: list[str] or list[int] = None,
               confirmation: bool = False) -> str or bool:
    check = False
    # This loop will run continuously until the user provides a valid input
    while check is False:
        separator(phr1)
        print(phr1)
        choices(accepted_choices)
        # Prompt the user to input a value and remove any trailing and leading zeroes
        val = input()
        val = val.strip()
        # Loop through each value in the accepted_choices list
        for val2 in accepted_choices:
            skip = False
            # Check if the input is a valid number
            if val.isdigit():
                if float(val) == 0:
                    skip = True
                if int(val) <= len(accepted_choices) and not skip:
                    # Check if the code is running a confirmation() and send back the respective values
                    if confirmation is True:
                        if int(val) == 1:
                            return True
                        if int(val) == 2:
                            return False
                    # If we are not trying to confirm a statement, print a separator and return the value
                    separator(phr1)
                    return accepted_choices[int(val) - 1]
                elif int(val) == val2:
                    return val2
            # Check if the input is a valid string (Capitalization is inconsequential)
            elif val.upper() == val2.upper() and not skip:
                # Check if the code is running a confirmation() and send back the respective values
                if confirmation is True:
                    if val2.upper() == stor.phr_verification[0].upper():
                        return True
                    if val2.upper() == stor.phr_verification[1].upper():
                        return False
                # If we are not trying to confirm a statement
                separator(phr1)
                return val2
        # If a valid input is not entered, print the following message
        print("Error. You have entered an invalid option.")

# This function will print the options the user can choose to the screen
# Usage of all arguments:
#       accepted_choices: a list of strings that stores the acceptable choices a user can input
# This function has no return value
def choices(accepted_choices: list[str] or list[int]) -> None:
    for idx in range(len(accepted_choices)):
        # If the choice is a string, capitalize it (if not already capitalized) and print it to the screen
        if str_to_float(accepted_choices[idx]) is None and accepted_choices[idx][0].islower():
                accepted_choices[idx] = accepted_choices[idx].capitalize()
        print("[{}] {}".format(idx+1, accepted_choices[idx]))


# This function will ask the user to confirm their input and reprompt the question if necessary.
# Usage of all arguments:
#       orig_val: A string that stores the user's choice
#       phr1_con: A String that should be created unformatted, but with the intention of being formatted
#                   by the orig_val. It represents the confirmation phrase that will ask the user if
#                   they are certain of their choice
#       accepted_choices: An OPTIONAL list of String objects that stores the acceptable choices that a
#                           user can input
#       obj_dict: an OPTIONAL dictionary filled with the attributes of every object in a created class
# This function will return the user's new input.
def confirm(orig_val: str, phr1_con:str, phr_reprint: str,  accepted_choices: list[str] = None,
            obj_dict: dict = None) -> str:
    run_loop = True
    # This loop will run until the user is certain of their choice
    while run_loop is True:
        user_certainty = user_input(phr1_con.format(orig_val), stor.phr_verification, True)
        # If the user wants to re-input a value, the code will check if any input can be provided.
        if user_certainty is False:
            if accepted_choices is None:
                orig_val = input(phr_reprint + "\n")
            else:
                orig_val = user_input(phr_reprint, accepted_choices)
                if obj_dict is not None:
                    print_stats(orig_val, obj_dict)
        # If the user does not want to re-input a value, print a separator and break the loop
        else:
            separator(phr1_con.format(orig_val))
            run_loop = False
    return orig_val

# This function will prompt the user to enter any input to continue
# This function has no return value
def prompt1() -> None:
    input("\n[Continue]\n")

# This function will convert a string into a float if possible. This function is mainly used
#   to check if it is possible to convert a string into an integer or float. We can not just
#   use the .isdigit() function because .isdigit() doesn't work for negative numbers
# Usage of all arguments:
#       phr1: any string
# This function will return phr1 as a float if possible or None if not
def str_to_float(phr1: str) -> float or None:
    try:
        return float(phr1)
    except ValueError:
        return None

# This function will create a separator that is the same length as its parameter
# Usage of all arguments:
#       phr1: any string
# This function has no return value
def separator(phr1:str) -> None:
    print("-"*len(phr1))

# This function will print the attributes associated with the embedded dictionary in such a way that
#   the name of the entity is printed first, the description is printed next (if provided), and the
#   attributes of the entity are printed last
# Usage of all arguments:
#       orig_val: A string that stores the user's choice
#       obj_dict: A dictionary filled with the attributes of every object in a created class
#                   or to be used in a specific scenario.
# This function has no return value
def print_stats(orig_val: str, obj_dict: dict) -> None:
    l2 = []
    # Run a loop for each key in the dictionary
    for key in obj_dict:
        if key.upper() == orig_val.upper():
            print("You have chosen: ")
            # This loop will check each key in the embedded dictionary and if the value of the
            #   embedded dictionary matches the user's input, then it will be printed to the screen.
            #   If a "Description" key exists in the embedded dictionary, then it will also be printed
            #   to the screen. It will store the other key-value pairs of the embedded dictionary
            #   into l2
            for val in obj_dict[key]:
                if str_to_float(obj_dict[key][val]) is None:
                    if obj_dict[key][val].upper() == orig_val.upper():
                        print(val + ":", obj_dict[key][val])
                        if obj_dict[key].get("Description") is not None:
                            print("\n" + "Description:", obj_dict[key]["Description"] + "\n")
                else:
                    l2.extend([[val, obj_dict[key][val]]])
            # Print the key-value pairs stored in l2
            for idx in range(len(l2)):
                if idx == len(l2)-1:
                    print(l2[idx][0] + ":", l2[idx][1])
                else:
                    print(l2[idx][0] + ":", l2[idx][1], end = "")
                    print(", ", end = "")
