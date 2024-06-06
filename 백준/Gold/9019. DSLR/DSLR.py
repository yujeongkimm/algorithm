from collections import deque

def character_changed(l, num):
    if l == 'D':
        return (num * 2) % 10000
    if l == 'S':
        return num-1 if num > 0 else 9999
    if l == 'L':
        return (num%1000)*10 + num//1000
    if l == 'R':
        return (num%10)*1000 + num//10

def commands():
    q = deque()
    q.append((x, ''))
    visited[x] = True

    while q:
        n, c = q.popleft()

        if n==y:
            print(c)
            return

        for l in ['D', 'S', 'L', 'R']:
            _n = character_changed(l, n)
            if not visited[_n]:
                q.append((_n, c + l))
                visited[_n]=True



t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    visited = [False] * 100000
    commands()
