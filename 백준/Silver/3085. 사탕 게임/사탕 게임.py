n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(input()))

# 2. 배열의 행마다 같은 색 몇개 있는지 계산
def calculate_row():
    global ans
    for row in range(n):
        cnt=1
        for col in range(n-1):
            if arr[row][col]==arr[row][col+1]:
                cnt+=1
                ans=max(cnt,ans)
            else:
                cnt=1
# 2. 배열의 열마다 같은 색 몇개 있는지 계산
def calculate_col():
    global ans
    for col in range(n):
        cnt=1
        for row in range(n-1):
            if arr[row][col]==arr[row+1][col]:
                cnt+=1
                ans=max(cnt,ans)
            else:
                cnt=1 # 초기화

ans=0
for i in range(n):
    for j in range(n):
        # 1. 오른쪽, 아래 쌍 교환
        if i+1<n and arr[i][j]!=arr[i+1][j]: # 아래쪽 비교
            arr[i][j],arr[i+1][j]=arr[i+1][j],arr[i][j] # 바꾸기
            calculate_row() # 2. 교환하면서 가장 긴 연속 색 찾기
            calculate_col()
            arr[i][j],arr[i+1][j]=arr[i+1][j],arr[i][j] # 3. 복구
        if j+1<n and arr[i][j]!=arr[i][j+1]: # 오른쪽 비교
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]
            calculate_row()
            calculate_col()
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]
print(ans)