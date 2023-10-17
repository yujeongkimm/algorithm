import heapq
import sys
n=int(sys.stdin.readline())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

arr.sort()
q=[arr[0][1]] #가장 먼저 끝나는 수업

for idx in range(1, n):
    if arr[idx][0]<q[0]: #시작시간이랑, 가장 빨리 끝나는 수업의 종료시간 비교
        #강의실 하나 더 필요
        heapq.heappush(q, arr[idx][1]) # 종료시간, 정렬
    else:
        heapq.heappop(q) #가장 작은 원소 빼기
        heapq.heappush(q, arr[idx][1]) # 종료시간, 정렬
print(len(q))