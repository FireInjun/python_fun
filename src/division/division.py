if __name__ == '__main__':
    a = int(input())
    b = int(input())


def int_div(a, b):
    return a // b


def float_div(a, b):
    return a / b


div_tuple = int_div(a, b), float_div(a, b)

for n in div_tuple:
    print(n)
