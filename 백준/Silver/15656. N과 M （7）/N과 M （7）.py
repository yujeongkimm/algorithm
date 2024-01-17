n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

ans=[0]*m

def recursion(depth):
    if depth==m:
        print(*ans)
        return

    for i in range(n):
        ans[depth]=arr[i]
        recursion(depth+1)

recursion(0)