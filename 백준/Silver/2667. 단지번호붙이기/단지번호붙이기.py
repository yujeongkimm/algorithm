n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 범위체크
    if x<0 or x>=n or y<0 or y>=n:
        return False

    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0  # 방문처리
        # 상,하,좌,우 탐색
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


result = []
cnt = 0  # 개수
count = 0  # 단지수
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result.append(cnt)
            # 단지완성
            count += 1
            cnt = 0
result.sort()
print(count)
for i in result:
    print(i)