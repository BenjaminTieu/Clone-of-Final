# This function will ask the user for an input. If the input is not an expected value, then the user will be re-prompted
def user_input(phr1:str, accepted_choices: list):
    check = False
    # This while loop will force the program to run until it gets an expected value
    while check is False:
        # Include a seperator between the user input and the dialogue
        for idx in range(len(phr1)):
            print("-", end = "")
        val = str(input("\n" + phr1 + "\n"))
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
                    for idx in range(len(phr1)):
                        print("-", end="")
                    print("\n", end = "")
                    return float(val)
            # Check if the input is a valid String (Capitalization is inconsequential)
            elif check_string and isinstance(val2, str):
                if val.upper().strip() == val2.upper().strip():
                    for idx in range(len(phr1)):
                        print("-", end="")
                    print("\n", end="")
                    return val2
        print("Error. You have entered an invalid option.")

def prompt1():
    input("\n[Continue]\n")