def get_fibonacci_series(input_value):
    fibonacci_series = [1]
    series_length = int(input_value)
    if series_length > 1:
        fibonacci_series.append(1)
        for i in range(2, series_length):
            fibonacci_series.append(fibonacci_series[i-2] + fibonacci_series[i-1])
    print(fibonacci_series)


length = input("Enter the length of the series you want to print: ")
get_fibonacci_series(length)