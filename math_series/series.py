def fibonacci(num):
    """
    DOCSTRING: Function returns the value of the num within the fibonacci
    sequence for a given position (num)
    """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)


def lucas(num):
    """
    DOCSTRING: Function returns the value of the num within the lucas
    sequence for a given position (num)
    """
    if num == 0:
        return 2
    elif num == 1:
        return 1
    else:
        return lucas(num - 1) + lucas(num - 2)


def sum_series(num, start_num=0, second_num=1):
    """
    Sum series, returns the given value at index (num) of a series of numbers,
    where the start_num is the first num in the series, and second_num is the second, with each
    set of the two previous numbers being added together.
    """
    if num == 0:
        return start_num
    elif num == 1:
        return second_num
    else:
        return sum_series(num-1, start_num, second_num) + sum_series(num-2, start_num, second_num)

