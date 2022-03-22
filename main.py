lists = [0] * (4+6+1)

for a in range(1, 5):
    for b in range(1, 7):
        lists[a+b] += 1

for i in range(4+6+1):
    if lists[i] == max(lists):
        print(i, end=' ')
