import sys

a = list(map(int, sys.stdin.readline().split()))

if a == sorted(a):
    print("ascending")
elif a == list(reversed(sorted(a))):
    print("descending")
else:
    print("mixed")

# print(a, reversed(sorted(a)))