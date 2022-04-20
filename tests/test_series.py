from series import fibonacci, lucas, sum_series


def test_fibonacci_for_int():
    assert type(fibonacci(3)) is int


def test_fibonacci_value_6():
    assert fibonacci(6) is 8


def test_fibonacci_value_10():
    assert fibonacci(10) is 55


def test_lucas_for_int():
    assert type(lucas(3)) is int


def test_lucas_for_value_5():
    assert lucas(5) is 11


def test_lucas_for_value_10():
    assert lucas(10) is 123


def test_sum_series_for_int():
    assert type(sum_series(2)) is int


def test_sum_series_for_fib():
    assert sum_series(5, 0, 1) is 5


def test_sum_series_for_lucas():
    assert sum_series(5, 2, 1) is 11


def test_sum_series_series():
    assert sum_series(5, 0, 2) is 10


"""
def test_one():
    actual = fizz_buzz(1)
    expected = "1"
    assert actual == expected
"""