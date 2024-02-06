# Problem-14: Obtain n*n values from user, and print an nxn matrix on the console.
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
    print(n)
    # Initialize an empty list with name 'nxn' containing only one empty list to start with:
    nxn: list = [[]]
    # Add n empty lists in the list nxn:
    # for i in range(0, n):
    #     nxn.append([])
    # print(nxn)
    count: int = 0  # number of inputs received from the user so far.
    row: int = 0  # Initialized a variable to store the value of the current row in the iteration.
    # Iterate through the loop until n*n values are registered:
    print(n * n)
    while row in range(0, n):
        print("Current row count: " + str(row + 1))
        try:
            current_input: int = int(input("Please enter the next integer value for an nxn matrix: "))
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
            print("Total values registered so far: " + str(count))
            print("Values registered for the current row so far: " + str(count - (row * n)))
            print("Values remaining in the current row: " + str(((row + 1) * n) - count))
        except ValueError:
            print("The entered value is invalid.")
    print("The desired nxn matrix:")
    print(nxn)


create_nxn_matrix()
