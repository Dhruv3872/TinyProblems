# Problem-1: How to remove characters from the first String which are present in the second String?
def remove_characters(first: str, second: str):
    # Note: Assumption: A solution that distinguishes an upper case letter and a lower case letter
    # as two distinct characters is acceptable.
    for c in second:
        first = first.replace(c, "")  # We need to assign the result back to the original string since
    # strings are immutable in Python. So any string method returns a new string. It does not change
    # the original string.
    return first


# Obtain input from the user:
first_string: str = input("Enter the string from which you want to remove characters: ")
second_string: str = input("Enter the string containing the characters you want to "
                           "remove from the first string: ")
print(remove_characters(first_string, second_string))
