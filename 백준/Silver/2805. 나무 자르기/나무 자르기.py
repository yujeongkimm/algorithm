# mid가 절단기 높이 -> 성공(m보다 크다) -> 후보o
# -> 절단한 나무 길이 줄여야됨 = 절단기의 높이는 증가해야 함 -> start = mid+1

# mid가 절단기 높이 -> 실패(자른 나무 길이가 m보다 작다) ->
# 절단기 높이 줄어야함 -> end = mid - 1

n,m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()
start, end = 0, max(tree)
while start<=end:
    mid=(start+end)//2
    sum=0
    for i in tree:
        if i>=mid:
            sum+=i-mid
    if sum>=m:
        start=mid+1
    else:
        end=mid-1
print(end)