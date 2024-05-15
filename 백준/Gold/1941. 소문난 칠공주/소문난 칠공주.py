from collections import deque

def calculate(index):
    r = index // 5
    c = index % 5
    return r,c


# 7명 학생 붙어있는지 확인
def bfs(pick):
    q = deque()
    q.append(pick[0])

    visited = [False]*7
    visited[0] = True

    while q:
        new = q.popleft()

        for dir in [-5,5,-1,1]:
            moved = new + dir

            if dir == 1 and moved%5==0:
                continue

            if dir == -1 and moved%5==4 :
                continue

            if 0<=moved<25 and moved in pick:
                index = pick.index(moved)
                if not visited[index]:
                    q.append(moved)
                    visited[index]=True

    return False if False in visited else True

students=[]
for _ in range(5):
    students.append(input())


# 학생 7명 구하기
pick=[]
def combinations(student_num):
    global pick
    if len(pick)==7:
        count=0
        for p in pick:
            r,c=calculate(p)
            if students[r][c] == 'S':
                count+=1
        if count < 4:
            return 0

        if bfs(pick):
            return 1
        return 0

    if student_num >=25:
        return 0

    ret = combinations(student_num+1) # 학생 포함 X
    pick.append(student_num) # 학생 포함
    ret += combinations(student_num+1)
    pick.pop()

    return ret

result = combinations(0)
print(result)