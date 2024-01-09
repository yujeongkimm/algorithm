n,b,w=map(int,input().split())
rocks=input()

ans,right_idx,white_count,black_count=0,0,0,0

for i in range(n):
    while right_idx<n:
        if black_count==b and rocks[right_idx]=='B':
            break
        if rocks[right_idx]=='W':
            white_count+=1
        else:
            black_count+=1
        right_idx+=1

    if white_count>=w:
        ans=max(ans, right_idx-i)
    if rocks[i]=='W':
        white_count-=1
    else:
        black_count-=1

print(ans)