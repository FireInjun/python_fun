if __name__ == '__main__':
    a = int(input())
    b = int(input())


def line_one(a, b):  # The first line contains the sum of the two numbers.
    return a + b


def line_two(a, b):  # The second line contains the difference of the two numbers(first - second).
    return a - b


def line_three(a, b):  # The third line contains the product of the two numbers.
    return a * b


line_tuple = line_one(a, b), line_two(a, b), line_three(a, b)

for n in line_tuple:
    print(n)
