# Problem-15: Obtain n*n values from user, and print an nxn matrix on the console.
def create_nxn_matrix():
    # 1. Get the value of n from the user for an nxn matrix:
    n: int = 0  # Initialised the value of n as 0, which will be made invalid in the next line.
    while (type(n) is not int) | (n <= 0):
        try:
            n: int = int(input("Please enter a positive integer as the value of n for an nxn matrix: "))
            if n <= 0:
                print("The entered value is not a positive integer.")
        except ValueError:
            print("The entered value is not a positive integer.")
    # Initialize an empty list with name 'nxn' containing only one empty list to start with:
    nxn: list = [[]]
    count: int = 0  # number of inputs received from the user so far.
    row: int = 0  # Initialized a variable to store the value of the current row in the iteration.
    column: int = 0  # Initialized a variable to store the value of the current column
    # in the iteration.
    # Iterate through the loop until n*n values are registered:
    while row in range(0, n):
        try:
            current_input: int = int(input("Please enter an integer value for the "
                                           "position at row " + str(row + 1) + " column "
                                           + str(column + 1) + " of the " + str(n) + "x" + str(n)
                                           + " matrix: "))
            # If the current row needs element(s):
            if len(nxn[row]) < n:
                # Add current_input at the end of the current row:
                nxn[row].append(current_input)
                count += 1
                # If the current row is now full:
                if len(nxn[row]) == n:
                    # If the next row is needed:
                    if count < (n * n):
                        # Increment the row count:
                        row += 1
                        # Add an empty list at the end of the list for this row:
                        nxn.append([])
                    else:
                        # Break out of the loop:
                        break
            column = count - (row * n)
        except ValueError:
            print("The entered value is invalid.")
    print("The desired " + str(n) + "x" + str(n) + " matrix:")
    print(nxn)
    return nxn

