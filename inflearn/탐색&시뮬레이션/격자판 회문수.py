a = [list(map(int, input().split())) for _ in range(7)]
cnt=0

for i in range(3):
    for j in range(7):
        temp = a[j][i:i+5]
        if temp == temp[::-1]:
            cnt+=1
        for k in range(2):
            if a[i+k][j] != a[i+5-1-k][j]:
                break
        else:
            cnt+=1

print(cnt)