n,m=map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
# 절단기 높이 = mid
# 자른 나무 길이 < m => 가져가는 나무 길이 늘림 => 절단기 높이 줄어야함 => 범위 less
# 자른 나무 길이 > m => 성공 => 최소값을 만족하는 절단기 높이 구해야함 => 가져가는 나무 길이 줄임 => 절단기 높이 늘림 => 범위 more
# ❔ 자른 나무 길이 = m => 성공 => 더 높이 잘라도 됨?? =>
# ❔start가 end보다 커지는 순간 => end가 절단기 높이 최대값
# 10 15 17 20
start,end=0,max(arr)
result=0
while start<=end:
    mid=(start+end)//2
    sum=0
    for i in arr:
        if i>=mid:
            sum+=i-mid
    if sum>=m:
        start=mid+1
    else:
        result = mid
        end=mid-1
print(result) # 절단기 높이 최대값