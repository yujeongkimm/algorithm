import sys
sys.setrecursionlimit(100000)

r,c=map(int,input().split())
graph=[]
for _ in range(r):
    graph.append(list(map(str, input())))
# 영역에서 #가 아니면 탐색
def dfs(x,y):
    if x<=-1 or x>=r or y<=-1 or y>=c:
        return False
    # 범위체크
    if graph[x][y]!='#':
        global wolf_cnt, sheep_cnt
        if graph[x][y]=='v':
            wolf_cnt+=1
        if graph[x][y]=='o':
            sheep_cnt+=1
        # 탐색할 수 있다.
        graph[x][y]='#' #방문처리
        # 상,하,좌,우
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

total_sheep, total_wolf = 0,0
sheep_cnt=0 #영역 안 양의 수
wolf_cnt=0 # 영역 안 늑대 수
for i in range(r):
    for j in range(c):
        if dfs(i,j)==True: # 구간 탐색 완료
            # 영역 안에 양의 수가 더 많으면
            if sheep_cnt > wolf_cnt:
                total_sheep+=sheep_cnt
            else:
                total_wolf+=wolf_cnt

            sheep_cnt, wolf_cnt = 0,0 # 초기화
print(total_sheep, total_wolf)
