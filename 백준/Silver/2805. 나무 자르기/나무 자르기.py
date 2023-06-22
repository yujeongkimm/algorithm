n,m=map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
# 절단기 높이 = mid
# 자른 나무 길이 < m => 가져가는 나무 길이 늘림 => 절단기 높이 줄어야함 => 범위 less
# 자른 나무 길이 > m => 성공 => 최소값을 만족하는 절단기 높이 구해야함 => 가져가는 나무 길이 줄임 => 절단기 높이 늘림 => 범위 more
# 자른 나무 길이 = m => 성공 => 루프문 빠져나가야 함 => start값 조절
# ❔start가 end보다 커지는 순간 => end가 절단기 높이 최대값
# 10 15 17 20
start,end=0,max(arr)
while start<=end:
    mid=(start+end)//2
    res=0
    for tree in arr:
        if tree>mid:
            res+=tree-mid
    if res<m:
        end=mid-1
    else:
        start=mid+1
print(end)