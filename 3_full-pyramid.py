# Code to print a full pyramid of characters based on
# user input.

# Function to obtain inputs necessary for the application:
def obtain_inputs():
    character: str = ""  # The character to be printed as the building block of pyramid.
    while character == "" or len(character) > 1:
        character = input("Enter the character you want as the building block of your Pyramid, for example: *: ")
    error = "none"  # Initialised a variable to store an exception
    steps = 0  # Number of steps of the pyramid. This is an input to be taken from the user.
    # Value 0 for 'steps' is invalid.
    # Loop while a positive integer is not entered as the desired steps of the pyramid:
    while error == "none" or error == ValueError or steps == 0:
        try:
            error = ""  # Changed the value of 'error' to break out of the loop in case of an acceptable input.
            steps = int(input("Enter the number of steps you want for the pyramid as a whole positive integer, "
                              + "for example: 5:  "))
        except ValueError as e:
            error = e
            print("Error: " + str(e))
    inputs: dict = {"character": character, "steps": steps}
    return inputs


# Function to create a full-pyramid string:
def create_full_pyramid(user_inputs: dict):
    character: str = user_inputs["character"]
    number_of_lines: int = user_inputs["steps"]
    output = ""  # Initialised the output string as empty.
    for i in range(1, number_of_lines + 1):
        output += " " * (number_of_lines - i)
        output += (character + " ") * i
        output = output[:len(output) - 1]  # To remove a " " at the end of the string. This is a requirement
        # of the implemented logic.
        output += " " * (number_of_lines - i) + "\n"
    output = output[:len(output) - 1]  # To remove the redundant new line character at the end of the string.
    return output


play: bool = True  # Play the game until you don't want to.
while play:
    print("\n")  # Restart the game with a one-line space.
    pyramid = create_full_pyramid(obtain_inputs())
    print(pyramid)
    play = not bool(input("Press Enter to continue playing. Type anything and press Enter to quit: "))
