# This function will ask the user for an input. If the input is not an expected value, then the user will be re-prompted
def user_input(phr1:str, accepted_choices: list):
    check = False
    # This while loop will force the program to run until it gets an expected value
    while check is False:
        # Include a seperator between the user input and the dialogue
        for idx in range(len(phr1)):
            print("-", end = "")
        print("\n" + phr1)
        choices(accepted_choices)
        val = input()
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
                    for idx in range(len(phr1)):
                        print("-", end="")
                    print("\n", end = "")
                    return accepted_choices[int(val)-1]
            # Check if the input is a valid String (Capitalization is inconsequential)
            elif check_string and isinstance(val2, str):
                if val.upper().strip() == val2.upper().strip():
                    for idx in range(len(phr1)):
                        print("-", end="")
                    print("\n", end="")
                    return val2
        print("Error. You have entered an invalid option.")

# This function will, given a list of accepted choices, print the available options to the screens with numbers
# associated with the respective choices
def choices(accepted_choices: list):
    for idx in range(len(accepted_choices)):
        # Simply print the choice to the screen
        if str_to_float(accepted_choices[idx]) is None:
            # Capitalize the first letter of the choice if it is not capitalized
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

# This function will prompt the user to enter any input to continue
def prompt1():
    input("\n[Continue]\n")

# This function

# This function will convert a string into a float if possible. If it is not possible, it will return None
def str_to_float(phr1: str) -> float or None:
    try:
        return float(phr1)
    except ValueError:
        return None