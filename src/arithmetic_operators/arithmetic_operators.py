if __name__ == "__main__":
    a = int(input())
    b = int(input())


def sum_int(a, b):
    """ Return the sum of two *numbers*."""
    return a + b


def diff_int(a, b):
    """ Return difference of  two *numbers*."""
    return a - b


def prod_int(a, b):
    """Return the product of the two *numbers*."""
    return a * b


def solution(a, b):
    """Print each value in the tuple 'line_tuple' on a new line."""
    line_tuple = sum_int(a, b), diff_int(a, b), prod_int(a, b)
    for n in line_tuple:
        print(n)
