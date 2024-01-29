# 계란 깻을 때, 상대방의 무게만큼 - , 음수면 깨짐
# 현재와 깨지지 않는 계란 중 비교

def check(arr):
    count=0
    for egg in arr:
        if egg[0]<=0:
            count+=1

    return count

answer=0
def recur(n, arr):
    global answer
    if n==N:
        count = check(arr)
        answer=max(answer, count)
        return

    if arr[n][0]<=0:
        recur(n+1, arr)
    else:
        is_all_broken=True
        for i in range(len(arr)):
            if i==n:
                continue
            if arr[i][0]>0:
                is_all_broken=False
                arr[n][0] -= arr[i][1]
                arr[i][0] -= arr[n][1]

                recur(n+1, arr)

                arr[n][0] += arr[i][1]
                arr[i][0] += arr[n][1]

        if is_all_broken:
            recur(n+1, arr)

N=int(input())
arr=[]
for _ in range(N):
    s,w=map(int,input().split())
    arr.append([s,w])

recur(0,arr)
print(answer)