n, m = map(int, input().split())
cnt = [0]*(n+m+3)

for a in range(1, n+1):
    for b in range(1, m+1):
        cnt[a+b] += 1

# 최대값 찾기
val = max(cnt)

for i in range(n+m+1):
    if cnt[i] == val:
        print(i, end=' ')