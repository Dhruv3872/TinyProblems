# Problem-13: Obtain 4 values from the user, and print a 2x2 matrix on the console.


def create_2x2_matrix():
    count: int = 0  # number of inputs received from the user so far.
    inputs: list = [[], []]  # Declaring an empty array.
    # print(inputs.shape)
    while count < 4:
        try:
            current_input: int = int(input("Please enter an integer value for the 2x2 matrix: "))
            if len(inputs[0]) < 2:
                inputs[0].append(current_input)
            else:
                inputs[1].append(current_input)
            count += 1
            print("Values registered so far: " + str(count))
        except ValueError:
            print("The entered value is invalid.")
    print("The desired 2x2 matrix:")
    print(inputs)


create_2x2_matrix()
