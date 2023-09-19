def solution(park, routes):
    answer = []
    x, y = 0, 0  # 시작 위치
    for row in range(len(park)):
        for col in range(len(park[0])):
            if park[row][col] == 'S':
                x, y = row, col
    # 이동 방향 정의
    op = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

    # 이동
    for route in routes:
        dx, dy = op[route.split()[0]]  # 이동 방향
        n = int(route.split()[1])  # 이동 횟수

        xx, yy = x, y
        canmove=True
        for i in range(n):  # 이동 반복
            nx = xx + dx  # 이동한 위치
            ny = yy + dy

            if 0 <= nx <= len(park) - 1 and 0 <= ny <= len(park[0]) - 1 and park[nx][ny] != 'X':
                canmove=True
                xx, yy = nx,ny
            else:
                canmove=False
                break
        print(canmove)
        if canmove:
            x = xx
            y = yy

    answer = [x, y]
    return answer