# Problem-17: Addition of two matrices:
# main function:
# l for list:
def addition_of_two_matrices(l1: list, l2: list):
    # Are both the lists matrices?
    if is_eligible_matrix(l1) and is_eligible_matrix(l2):
        # Are both of them number matrices? i.e.
        # Made up of integers or floats or complex numbers?
        if is_number_matrix(l1) and is_number_matrix(l2):
            # Are the two of them compatible with each other?
            if are_compatible(l1, l2):
                # Perform addition on them.

                return add_two_matrices(l1, l2)
    return False


# Function to check if a list is an eligible matrix:
# To be one, all of its rows must have the same number of elements.
def is_eligible_matrix(given_list: list):
    if len(given_list) == 0:
        # print('ineligible')
        return False
    elif len(given_list) == 1:
        if type(given_list[0]) is not list:
            # print('eligible')
            return True
        else:
            # print('ineligible')
            return False
    else:
        rows: int = len(given_list)
        # Initialize a variable for columns with an invalid value:
        columns: int = -1
        # A matrix may be of m x 1 or 1 x m, too. To distinguish between these two:
        is_row_singleton: bool = False  # Will be set to True if the first
        # column is a singleton value, because in that case, the corresponding
        # matrix will have only one row while having number of columns equal to
        # the length of the list.
        for row in range(0, rows):
            # If variable 'columns' has its default value, set it:
            if columns == -1:
                if type(given_list[row]) is not list:
                    # Assume that it's not any other collection type.
                    # Assume that it will be a single value of type int, float,
                    # complex, str, or any other.
                    is_row_singleton = True
                    columns = rows
                    break
                else:
                    columns = len(given_list[row])  # This value has to be
                    # constant for every row that follows.
            # Else, check if the length of the current row matches
            # the value of 'columns' variable :
            elif type(given_list[row]) is not list:
                # print('ineligible')
                return False  # Every row should be of the same length.
            elif len(given_list[row]) != columns:
                # print('ineligible')
                return False  # Every row should be of the same length.
        if is_row_singleton:
            # 'columns' variable will have the length of the list, and we need to reassign 'rows'
            # variable value 1:
            rows = 1
            for column in range(0, columns):
                if type(given_list[column]) is list:
                    # print('ineligible')
                    return False
        # print('eligible')
        return True


# Function to determine if the given matrix is a number matrix
# i.e. if it contains only integers, float, and/or complex numbers or not:
# m for matrix:
def is_number_matrix(m: list):
    if len(m) == 1:
        if (type(m[0]) is int) or (type(m[0]) is float) or (type(m[0]) is complex):
            # print('number')
            return True
        else:
            # print('not number')
            return False
    else:
        is_row_singleton: bool = False  # Initializing it with False.
        for row in range(0, len(m)):
            if type(m[row]) is not list:
                # This element is not a collection. Hence, according to our assumption,
                # it's a single value variable.
                # And this function will be executed only if the list passes
                # is_eligible_matrix function. Hence, all other elements must  also be
                # singleton. Hence, we must treat the values we were treating as rows
                # as columns now.
                is_row_singleton = True
                break
                # else is not needed after a break statement.
            for column in range(0, len(m[row])):
                if ((type(m[row][column]) is not int) and (type(m[row][column]) is not float)
                        and (type(m[row][column]) is not complex)):
                    # print('not number')
                    return False
        if is_row_singleton:
            # We need to evaluate the matrix for this special case as we broke out of the
            # evaluation when we found the first non-list element:
            for column in range(len(m)):
                if ((type(m[column]) is not int) and (type(m[column]) is not float)
                        and (type(m[column]) is not complex)):
                    # print('not number')
                    return False
        # print('number')
        return True


# Function to determine if the two given matrices are compatible matrices or not:
def are_compatible(m1: list, m2: list):
    result: bool = True  # Beginning with the assumption that they are compatible.
    if len(m1) != len(m2):
        result = False
    elif (type(m1[0]) is not list) or (type(m2[0]) is not list):
        if not ((type(m1[0]) is not list) and (type(m2[0]) is not list)):
            result = False
    elif len(m1[0]) != len(m2[0]):
        result = False
    # if result:
    #     print('compatible')
    # else:
    #     print('incompatible')
    return result


# Function to add two compatible number matrices:
def add_two_matrices(m1: list, m2: list):
    # Initialize an empty list to be ultimately provided as output:
    m: list = []
    rows: int = len(m1)
    if rows == 1:
        m.append(m1[0] + m2[0])
    else:
        if type(m1[0]) is not list:
            # This means that the matrix is made up of single value variables, not lists
            # as we will execute this function after passing the matrices through
            # eligibility and compatibility checking functions only.
            for row in range(0, rows):
                m.append(m1[row] + m2[row])
        else:
            columns: int = len(m1[0])
            # Add all the rows as empty lists:
            for row in range(0, rows):
                m.append([])
            for row in range(0, rows):
                for column in range(0, columns):
                    m[row].append(m1[row][column] + m2[row][column])
    # print(m)
    return m


# is_eligible_matrix([])
# is_eligible_matrix([0])
# is_eligible_matrix(['p'])
# is_eligible_matrix(['p', 'q'])
# is_eligible_matrix([['p'], ['q']])
# is_eligible_matrix([['p', 'q'], ['r', 's']])
# is_eligible_matrix([[1, 2], [3, 4]])
# is_eligible_matrix([1, 2, 3])
# is_eligible_matrix([[1], [2], [3]])
# is_eligible_matrix([1, ['a']])
# is_eligible_matrix([['a'], 1])
# is_eligible_matrix([['a'], 3, [4]])
# is_eligible_matrix([['1', 2], [3, 'f', 'k']])
# 
# is_number_matrix([0])
# is_number_matrix(['p'])
# is_number_matrix(['p', 'q'])
# is_number_matrix([['p'], ['q']])
# is_number_matrix([['p', 'q'], ['r', 's']])
# is_number_matrix([[1, 2], [3, 4]])
# is_number_matrix([1, 2, 3])
# is_number_matrix([[1], [2], [3]])
# 
# print(are_compatible([0], [1]))
# print(are_compatible([1, 2], [3, 4]))
# print(are_compatible([[1], [2]], [[3], [4]]))
# print(are_compatible([0], [[1]]))
# print(are_compatible([1, 2], [[3], [4]]))
# 
# add_two_matrices([55], [1])
# add_two_matrices([1, 2], [3, 4])
# add_two_matrices([[1], [2]], [[3], [4]])

# print(addition_of_two_matrices([], ['p']))
# print(addition_of_two_matrices(['q'], ['p']))
# print(addition_of_two_matrices([1], ['p']))
# print(addition_of_two_matrices([1], [4, 6]))
# print(addition_of_two_matrices([55], [1]))
# print(addition_of_two_matrices([1, 2], [3, 4]))
# print(addition_of_two_matrices([[1], [2]], [[3], [4]]))

print(addition_of_two_matrices([[1, 1.5, 1], [2 + 9j, 1, 2], [3, 3.1, 5]],
                               [[1.9, 4, 8.4j], [3, 3, 3], [2.5, 3.5, 1.6]]))
