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
    if num == 0:
        return start_num
    elif num == 1:
        return second_num
    else:
        return sum_series(num-1, start_num, second_num) + sum_series(num-2, start_num, second_num)


# sum_series(5, 0, 6)
# 6
# 0, 2, 2, 4, 6, 10, 16, 26
#
# 2, 2, 4, 6, 10, 16, 26 . . .