from collections import namedtuple

N = int(input()) # first line, number of students

student = namedtuple('student', input().strip().split()) # get student from input

print(sum(float(student(*input().strip().split()).MARKS) for _ in range(N))/N)