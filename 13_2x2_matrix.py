# Problem-13: Obtain 4 values from the user, and print a 2x2 matrix on the console.


def create_2x2_matrix():
    count: int = 0  # number of inputs received from the user so far.
    row: int = 1  # To keep track of the row number from the perspective of the user,
    # we initialized a variable with the value 1 (and not 0).
    column: int = 1  # To keep track of the column number from the perspective of the user,
    # we initialized a variable with the value 1 (and not 0).
    inputs: list = [[], []]  # Declaring an empty array.
    # print(inputs.shape)
    while count < 4:
        try:
            current_input: int = int(input("Please enter an integer value for the "
                                           "position at row " + str(row) + " column "
                                           + str(column) + " of the 2x2 matrix: "))
            if len(inputs[0]) < 2:
                inputs[0].append(current_input)
                # Increment the column count for the next iteration:
                column += 1
                if count == 1:
                    # Assign the row to value 2 and column to value 1 for the next iteration:
                    row = 2
                    column = 1
            else:
                if count == 2:
                    column = 2
                inputs[1].append(current_input)
            count += 1
            print("Values registered so far: " + str(count))
        except ValueError:
            print("The entered value is invalid.")
    print("The desired 2x2 matrix:")
    print(inputs)


create_2x2_matrix()
