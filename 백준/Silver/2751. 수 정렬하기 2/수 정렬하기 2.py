import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))


def mergeSort(l):
    if len(l) <= 1:
        return l

    mid = len(l) // 2

    left = mergeSort(l[:mid])
    right = mergeSort(l[mid:])

    return combine(left, right)


def combine(left, right):
    _sorted = []
    p1, p2 = 0, 0

    while len(left) > p1 and len(right) > p2:
        if left[p1] > right[p2]:
            _sorted.append(right[p2])
            p2 += 1
        else:
            _sorted.append(left[p1])
            p1 += 1

    while len(left) > p1:
        _sorted.append(left[p1])
        p1 += 1

    while len(right) > p2:
        _sorted.append(right[p2])
        p2 += 1

    return _sorted


for i in mergeSort(arr):
    print(i)