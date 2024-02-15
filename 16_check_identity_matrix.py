# Problem-16: Check if the given nxn matrix is an identity matrix.
from create_nxn_matrix import *


def check_identity_matrix(matrix: list):
    # Find out the length of the given matrix:
    given_length: int = len(matrix)
    # Create an identity matrix of the same length: m for matrix
    m: list = create_identity_matrix(given_length)
    # If both are identical, the given matrix is an identity matrix:
    if matrix == m:
        print(True)
        return True
    else:
        print(False)
        return False


def create_identity_matrix(length: int):  # l for length.
    # If the length is 1, return [1]:
    if length == 1:
        return [1]
    # The following code block will be executed only if the length is not 1, because otherwise,
    # the function would have returned [1]. So using 'else' is redundant here:
    # Initialize an empty list:
    # m for matrix:
    m: list = [[]]
    # Initialize a variable to keep track of the current row:
    row: int = 0
    # Initialize a variable to keep track of total entries so far:
    count: int = 0
    # Stay in the loop until row is less than the length:
    while row < length:
        if len(m[row]) < length:
            if len(m[row]) == row:
                m[row].append(1)
            else:
                m[row].append(0)
            count += 1
            if len(m[row]) == length:
                if count < (length * length):
                    m.append([])
                    row += 1
                else:
                    # The matrix has been created. Exit the loop:
                    break
    # Return the created matrix:
    return m


check_identity_matrix(create_nxn_matrix())
