# This function will ask the user for an input. If the input is not an expected value, then the user will be re-prompted
def user_input(phr1:str, accepted_choices: list = None, confirmation: bool = False):
    check = False
    # This loop will run continuously until the user inputs a valid input
    while check is False:
        seperator(phr1)
        print(phr1)
        choices(accepted_choices)
        # Prompt the user to input a value and remove any trailing and leading zeroes
        val = input()
        val = val.strip()
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
            if len(val) > 1 and check_string is False and contains_string is False and int(val[0]) == 0:
                check_string = True
            # Check if the input is a valid number
            if check_string is False and contains_string is False:
                if int(val) <= len(accepted_choices):
                    # Check if the code is running a confirmation() and send back the respective values
                    if confirmation is True:
                        if int(val) == 1:
                            return False
                        if int(val) == 2:
                            return True
                    # If we are not trying to confirm a statement, print a seperator and return the value
                    seperator(phr1)
                    return accepted_choices[int(val)-1]
            # Check if the input is a valid String (Capitalization is inconsequential)
            elif check_string and isinstance(val2, str):
                if val.upper().strip() == val2.upper().strip():
                    # Check if the code is running a confirmation() and send back the respective values
                    if confirmation is True:
                        if val2 == "Yes":
                            return False
                        if val2 == "No":
                            return True
                    # If we are not trying to confirm a statement
                    seperator(phr1)
                    return val2
        # If a valid input is not entered, print the following message
        print("Error. You have entered an invalid option.")

# This function will, given a list of accepted choices, print the available options to the screens with numbers
# associated with the respective choices
def choices(accepted_choices: list):
    for idx in range(len(accepted_choices)):
        # Simply print the choice to the screen
        if str_to_float(accepted_choices[idx]) is None:
            # Capitalize the first letter of the choice if it is not capitalized and print it to the screen along with
            # an associated number
            if accepted_choices[idx][0].upper() != accepted_choices[idx][0]:
                broken_phr = ""
                first_letter = accepted_choices[idx][0].upper()
                for idx2 in range(1, len(accepted_choices[idx])):
                    broken_phr += accepted_choices[idx][idx2]
                print("[{}] {}".format(idx+1,first_letter + broken_phr))
            else:
                print("[{}] {}".format(idx+1, accepted_choices[idx]))
        # Simply print the number to the screen if one of the accepted choices is a number
        else:
            print(accepted_choices[idx])

# This function will ask the user to confirm their input and reprompt the question if necessary. The function must be
# given the following arguments: the original input, the confirmation phrase that asks the user if they are sure about
# their input, and the question to be reprinted if the user wants to change their input.
# There are arguments that may be passed to the function if needed (omitted otherwise) such as a list of accepted
# choices and a dictionary of the class-specific objects.
# Please note that phr1_con (the confirmation phrase) should be an unformatted string that has the intention of being
# formatted.
def confirm(orig_val: str, phr1_con:str, phr_reprint: str,  accepted_choices_re: list = None,
            obj_dict: dict = None) -> str:
    run_loop = True
    phr_verification = ["Yes", "No"]
    # This loop will run until the user is certain of their choice
    while run_loop is True:
        input_confirm = user_input(phr1_con.format(orig_val), phr_verification, True)
        # If the user wants to re-input a value, the code will check if any input can be provided.
        if input_confirm is True:
            if accepted_choices_re is None:
                orig_val = input(phr_reprint + "\n")
            else:
                orig_val = user_input(phr_reprint, accepted_choices_re)
                # If the function is given a dictionary of class-specific objects to compare with, run the following
                if obj_dict is not None:
                    print_stats(orig_val, obj_dict)
        # If the user does not want to re-input a value, print a seperator and break the loop
        else:
            seperator(phr1_con)
            run_loop = False
    return orig_val

# This function will prompt the user to enter any input to continue
def prompt1():
    input("\n[Continue]\n")

# This function will prompt the user to enter any input to continue without printing a "continue" message
def prompt2():
    input()

# This function will convert a string into a float if possible. If it is not possible, it will return None
def str_to_float(phr1: str) -> float or None:
    try:
        return float(phr1)
    except ValueError:
        return None

# This function will create a seperator that is the same length as its parameter
def seperator(phr1:str):
    for idx in range(len(phr1)):
        print("-", end="")
    print("\n", end="")

# This function will print the attributes associated with the embedded dictionary in such a way that the name of the
# item is printed first, the description is printed next (if provided), and the stats of the item are printed last
def print_stats(orig_val: str, obj_dict: dict):
    last_val = ""
    # Run a loop for each key in the dictionary
    for key in obj_dict:
        # Check if the key matches the value provided by the user so that the code knows which
        # attributes it should print
        if key == orig_val:
            print("You have chosen: ")
            # This loop will check each key in the embedded dictionary and if the value of the embedded dictionary
            # matches the user's input, then it will be printed to the screen. If a "Description" key exists in the
            # embedded dictionary, then it will also be printed to the screen.
            for val in obj_dict[key]:
                last_val = val
                if obj_dict[key][val] == orig_val:
                    print(val + ":", end=" ")
                    print(obj_dict[key][val])
                    if obj_dict[key].get("Description") is not None:
                        print("\n" + "Description" + ":")
                        print(obj_dict[key]["Description"] + "\n")
            # This loop will check each key in the embedded dictionary and print
            # the missing attributes to the screen
            for main_attr in obj_dict[key]:
                if main_attr != "Description" and obj_dict[key][main_attr] != orig_val:
                    print(main_attr + ":", end=" ")
                    print(obj_dict[key][main_attr], end="")
                    if not main_attr == last_val:
                        print(", ", end = "")
            print("\n", end="")
