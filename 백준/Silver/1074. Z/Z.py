import sys
n,r,c=map(int,sys.stdin.readline().split())

ans=0

def recur(x,y,e):
    global ans
    if x==r and y==c:
        print(ans)
        exit(0)
        
    if e==1:
        ans+=1
        return
    
    if not (x<=r<x+e and y<=c<y+e):
        ans+=e*e
        return
    
    temp=e//2
    
    recur(x,y,temp)
    recur(x,y+temp, temp)
    recur(x+temp, y, temp)
    recur(x+temp, y+temp, temp)
    

recur(0,0,2**n)
        