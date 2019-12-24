if __name__ == "__main__":
    a = int(input())
    b = int(input())


def line_one(a, b):
    """ Return the sum of two *numbers*."""
    return a + b


def line_two(a, b):
    """ Return difference of  two *numbers*."""
    return a - b


def line_three(a, b):
    """Return the product of the two *numbers*."""
    return a * b


def solution(a, b):
    """Print each value in the tuple 'line_tuple' on a new line."""
    line_tuple = line_one(a, b), line_two(a, b), line_three(a, b)
    for n in line_tuple:
        print(n)
