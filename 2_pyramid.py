# Code to print a pyramid of characters left to right or right to left based on
# user input.
def print_pyramid(number_of_lines: int, direction: bool):
    character = "*"  # The character to be printed as the building block of pyramid.
    output = ""  # Initialised the output string as empty.
    if direction:
        for i in range(1, number_of_lines + 1):
            output = output + ((number_of_lines - i) * " ") + i * character + "\n"
    else:
        for i in range(1, number_of_lines + 1):
            output = output + i * character + "\n"
    output = output[:len(output) - 1]  # To remove the redundant new line character at the end of the string.
    print(output)


error = "none"  # Initialised a variable to store an exception
steps = 0  # Number of steps of the pyramid. This is an input to be taken from the user.
# Value 0 for 'steps' is invalid.
# Loop while a positive integer is not entered as the desired steps of the pyramid:
while error == "none" or error == ValueError or steps == 0:
    try:
        # print(error)
        error = ""  # Changed the value of 'error' to break out of the loop in case of an acceptable input.
        # print(error)
        steps = int(input("Enter the number of steps you want for the pyramid as a whole positive integer:  "))
    except ValueError as e:
        error = e
        print(e)
left_or_right: bool = bool(input("Type anything and then press Enter to get a right-to-left pyramid.\n"
                                 + "Directly press Enter for a left-to-right one: ")) # Empty string is False.
# Any other string will return True.
print_pyramid(steps, left_or_right)
