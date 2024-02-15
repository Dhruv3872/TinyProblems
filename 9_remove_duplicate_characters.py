# Remove duplicates from a given string:
# Note: We will assume that it is allowed for the output string to contain both
# upper and lower case characters if they are present in the input string.
def remove_duplicates(input_string: str):
    # Initialize an empty dictionary
    derived: dict = dict()
    output_string: str = ""  # Initialised an empty string to be returned at the end of this method.
    for c in input_string:
        exists: bool = derived.get(c, False)
        if not exists:
            derived[c] = 1
            output_string += c
    return output_string
# Time complexity of the above function: O(n)


given: str = input("Enter the string from which you want to remove duplicates: ")
print(remove_duplicates(given))
