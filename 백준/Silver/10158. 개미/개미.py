w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

time_x = t%(2*w)
time_y = t%(2*h)

current_x = p
dx = 1
# time_x 동안 x 이동
for _ in range(time_x):
    if current_x == w:
        dx = -1
    elif current_x == 0:
        dx = 1
    current_x += dx

current_y = q
dy = 1
# time_y 동안 y 이동
for _ in range(time_y):
    if current_y == h:
        dy = -1
    elif current_y == 0:
        dy = 1
    current_y += dy
print(current_x, current_y)
