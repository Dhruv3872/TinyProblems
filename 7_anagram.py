# Problem: Check if given 2 strings are anagram of each other:
def check_anagram(input1: str, input2: str):
    # How to go about it:
    # 1. Logic:
    # 	1. Count each character's occurances in the first string, and store in a variable.
    # 	2. Repeat this process for the second string.
    #	3. Compare these two variables. If they are identical, the strings are anagrams of each other.
    # 2. Code:
    # 	1. Create a function 'count_characters': It will take string as its input.
    # 		1. Initialise an empty dictionary.
    # 		2. Loop through the string:
    # 			1. The character at any given iteration will become a key of the dictionary.
    # 			If it already exists in the dictionary,  the corresponding value will be appended
    # 			by 1. Otherwise, the corresponding value will be set to 1.
    # 	2. Use this function for both of the strings to generate two dictionary objects.
    # 	3. Compare if the two objects are identical. That's it.
    input1_dictionary = string_to_dictionary(input1)
    input2_dictionary = string_to_dictionary(input2)
    if input1_dictionary == input2_dictionary:  # If both the objects are identical:
        return True  # The strings are anagrams of each other.
    else:
        return False


# Function to generate a dictionary object out of the input string having string's characters
# as its keys and their occurrences as its values:
def string_to_dictionary(input_string: str):
    output_dictionary: dict = dict()
    for c in input_string:
        if output_dictionary.get(c):
            # Continue to the next character if the key already exists.
            continue
        else:  # Count the occurrences of the character and add it to the dictionary object:
            output_dictionary[c] = input_string.count(c)
    print(output_dictionary)
    return output_dictionary


print(check_anagram("carnivorous", "coronavirus"))