n=int(input())
a=list(map(int,input().split()))
x=int(input())

'''
시간초과 
cnt=0
for i in range(n): # O(N)
    value=x-a[i]
    for j in range(i+1,n): # O(N)
        if a[j]==value:
            cnt+=1
print(cnt)
'''

# value 값 존재하는지 탐색하지 않고, 바로 알 수 있다면?
cnt=0
exits=[False]*1000001 # 1~1000000 까지 숫자 나왔는지
for i in a:
    exits[i]=True
for i in a: # O(N)
    value=x-i
    if value<=i:
        continue
    if 1<=value and value<=1000000:
        if exits[value]:
            cnt+=1
print(cnt)