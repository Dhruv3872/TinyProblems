# Problem-16: Check if the given nxn matrix is an identity matrix.
def check_identity_matrix(matrix: list):
    # Print matrix for easy validation of the result later on:
    print(matrix)
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


test1: list = [1]  # Should return True
test2: list = [4]  # Should return False
test3: list = [[2, 3], [0, 1]]  # Should return False
test4: list = [[1, 0], [0, 1]]  # Should return True
test5: list = [[0, 0], [0, 1]]  # Should return False
test6: list = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]  # Should return False
test7: list = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # Should return True
check_identity_matrix(test1)
check_identity_matrix(test2)
check_identity_matrix(test3)
check_identity_matrix(test4)
check_identity_matrix(test5)
check_identity_matrix(test6)
check_identity_matrix(test7)

# def create_matrix_from_input():
#     rows: int = int(input("Enter the number of rows present in your matrix: "))
#     columns: int = int(input("Enter the number of columns present in your matrix: "))
#     matrix: list = []
#     for i in range(0, rows):
#         for j in range(0, columns):
#
#
# create_matrix_from_input()
