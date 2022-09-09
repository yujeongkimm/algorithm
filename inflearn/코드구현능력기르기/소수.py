n = int(input())
'''
내풀이
val = 0
res = 0
for k in range(1, n+1):     # 1부터 n까지 -> k
    for i in range(1, k+1):     # k가 약수인지 판단
        if k%i ==0:
            val+=1
    if val == 2:
        res += 1
    val = 0
print(res)
'''

ch = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)