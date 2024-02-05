# Problem-14: Obtain 9 values from user, and print a 3x3 matrix on the console.


def create_3x3_matrix():
    count: int = 0  # number of inputs received from the user so far.
    inputs: list = [[], [], []]  # Declaring an empty array.
    row: int = 0
    while count < 9:
        while row in range(0,3):
            print("Current row count: " + str(row + 1))
            try:
                current_input: int = int(input("Please enter an integer value for a 3x3 matrix: "))
                if len(inputs[row]) < 3:
                    inputs[row].append(current_input)
                    if len(inputs[row]) == 3:
                        row += 1
                count += 1
                print("Values registered so far: " + str(count))
            except ValueError:
                print("The entered value is invalid.")
    print("The desired 3x3 matrix:")
    print(inputs)


create_3x3_matrix()
