# Problem-4: How to find the maximum occurring character in a given string?
def maximum_occurring_character(input_string: str):
    count: int = 0  # Initialise a count variable with 0.
    most_repetitive_character: str = ''
    for c in input_string:
        current_count = input_string.count(c)
        if current_count > count:
            count = current_count
            most_repetitive_character = c
            print(most_repetitive_character + ' : ' + str(count))
    return most_repetitive_character


given: str = input("Enter the string for which you want to find the maximum occurring "
                   "character: ")
print(maximum_occurring_character(given))
