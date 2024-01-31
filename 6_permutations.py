# Problem-2: Write all permutations of the given string
# Note: This one is unsolved as of this commit.
def permutations(input_string: str):
    # How to go about it:
    # 1. Which collection type should we use to store permutations?:
    # 'Set' since you can add and remove items from it, and it does not allow duplicates.
    permutation_set = set()  # Initialised an empty set to store permutations.
    permutation_set.add(input_string)
    # print(permutation_set)
    reference: str = input_string  # Begin while loop with input string as reference for
    # creating permutations.
    count_permutations = 1  # Initialised the permutation count with 1.
    length: int = len(input_string)
    chars_to_leave: int = 2
    while count_permutations < factorial(length):
        next_permutation: str = reference[:length - 2] + reference[length - 1] + reference[length - 2]
        if next_permutation not in permutation_set:
            permutation_set.add(next_permutation)
            count_permutations += 1
        else:
            chars_to_leave += 1
            # next_permutation = (next_permutation[:(length - (2 + chars_to_leave))] +
            #                     next_permutation[length - (2 + chars_to_leave + 1)] +
            #                     next_permutation[length - (2 + chars_to_leave)] +
            #                     next_permutation[(length - (2 + chars_to_leave) + 1):])
        print(next_permutation)
    # in_making: str = ""  # Current permutation in making.
    # tuple_from_string: tuple = tuple(input_string)
    # for
    # string_from_tuple: str = ''.join(tuple_from_string)
    # another_permutation: str =
    # return string_from_tuple
    return permutation_set


# Function created to use inside permutations function:
def factorial(n: int):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(10))
print(permutations("abc"))

# play: bool = True  # Play the game until you don't want to.
# while play:
#     print("\n")  # Restart the game with a one-line space.
#     input_string: str = input("Enter a string to print all possible permutations of it: ")
#     print(permutations(input_string))
#     play = not bool(input("Press Enter to continue playing. Type anything and press Enter to quit: "))
