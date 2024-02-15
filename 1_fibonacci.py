def get_fibonacci_series(input_value: str):
    fibonacci_series = [1]
    series_length: int = 0  # Initializing this variable with a value
    # that will be deemed invalid in the upcoming while loop's condition.
    error: str = 'none'  # Initializing the error variable with a value other than 'ValueError'.
    while series_length < 1 or error == ValueError:
        try:
            series_length = int(input_value)
            if series_length > 1:
                fibonacci_series.append(1)
                for i in range(2, series_length):
                    fibonacci_series.append(fibonacci_series[i - 2] + fibonacci_series[i - 1])
            elif series_length == 1:
                break
            else:
                input_value = input("Please enter a valid integer > 0 as the length "
                                    "of the series you want to print: ")
        except ValueError:
            input_value = input("Please enter a valid integer > 0 as the length "
                                "of the series you want to print: ")
    print(fibonacci_series)


length = input("Enter the length of the series you want to print: ")
get_fibonacci_series(length)

# Test case-3: If input number is larger than integer type size:
# According to Python documentation found here:
# https://docs.python.org/3/library/stdtypes.html#integer-string-conversion-length-limitation
# the int() function has a global default limit of 4300 digits, beyond which a ValueError
# is raised, but for the task at hand, i.e. for obtaining Fibonacci series, because of the
# nature of the function is recursive, the computer memory limit would be much smaller than
# 4300. Besides, between the input value of 20000 and 21000, the length of a single integer
# in the Fibonacci series crosses the mark of 4300 digits, which cannot be converted to
# a string, and hence, results in ValueError when we want to print the series on the console
# as the same limit is applied by default str() function, too for int to str conversion.
