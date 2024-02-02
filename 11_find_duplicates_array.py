# Problem-11: Find Duplicates in an array:
import numpy as np


def find_duplicates(input_array: np.ndarray):
    frequency: dict = dict()
    for x in input_array:
        exists = frequency.get(x, False)
        if not exists:
            frequency[x] = 1
        else:
            frequency[x] += 1
    duplicates: dict = dict()
    for x in frequency:
        value: int = frequency[x]
        if value > 1:
            duplicates[x] = value
    return duplicates


this_array: np.ndarray = np.array([1,1,5,6,8,9,8,7,5,13,4,5,4,6,2,8,1,9,7,2,11])
print(find_duplicates(this_array))
