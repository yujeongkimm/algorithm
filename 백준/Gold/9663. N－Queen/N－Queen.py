#pypy3
import sys

n = int(sys.stdin.readline())
arr = [0 for _ in range(n)]  # index: 행, 값: 열
sum = 0


def check(r1, c1, r2, c2):
    if c1 == c2:
        return True
    if r1 - c1 == r2 - c2:
        return True
    if r1 + c1 == r2 + c2:
        return True
    return False


def dfs(row):
    if row == n:
        global sum
        sum += 1
    else:
        for cand in range(n):  # 열
            possible = True
            for r in range(row):  # 이전 행들에 대해서 대각선, 열 값 같은지 확인:
                if check(row, cand, r, arr[r]):
                    possible = False
                    break
            if possible:
                arr[row] = cand
                dfs(row + 1)
                arr[row] = 0


dfs(0)
print(sum)
