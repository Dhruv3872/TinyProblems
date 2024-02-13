# Remove duplicates from a given string:
def remove_duplicates(input_string: str):
    input_set: set = set(input_string)  # Converted the input string to a set to remove duplicates
    # since sets in Python cannot have duplicates.
    output_string: str = ""  # Initialised an empty string to be return at the end of this method.
    for c in input_set:  # Add each element of the set to the output string.
        output_string += c
    return output_string


given: str = input("Enter the string from which you want to remove duplicates: ")
print(remove_duplicates(given))
