import sys
n=int(input())

w=[]
for _ in range(n):
    w.append(list(map(int,input().split())))

check=[False]*n
result=sys.maxsize

def recur(cnt, _sum, start, cur):
    global result
    if cnt==n and start==cur:
        result=min(_sum, result)
        return

    for i in range(n):
        if not check[i] and w[cur][i] != 0:
            check[i]=True
            recur(cnt+1, _sum + w[cur][i], 0, i)
            check[i]=False


recur(0, 0, 0, 0)

print(result)