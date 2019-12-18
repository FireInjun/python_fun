if __name__ == '__main__':
    n = int(input())

"""
Read an integer and print all numbers from 1 to integer on a single line
"""

temp_list = []
n_plus_one = n + 1
for num in range(1, n_plus_one):
    temp_list.append(num)

for i in temp_list:
    print(i, end="")
