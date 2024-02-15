# Problem-10: Write a program to find K’th smallest element in an unsorted array:
def kth_smallest_array_element(input_array: list, k: int):
    # Sort the input array:
    input_array.sort()
    print('sorted array: ' + str(input_array))
    return input_array[k-1]  # kth element is positioned at k-1 since arrays start at index 0.


this_array: list = [7, 5, 8, 5, 6, 3, 2, 1, 8, 9, 5, 4, 7, 6, 5]
k_value: int = 13  # Input value k for the function as in 'kth smallest element'. Play around by changing this value
# or by changing this_array.
print('kth smallest element: ' + str(kth_smallest_array_element(this_array, k_value)))
