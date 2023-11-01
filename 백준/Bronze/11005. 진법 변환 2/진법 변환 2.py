n,b=map(int,input().split())
char_list='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans=''
while n>0:
    ans+=(char_list[n%b])
    n = n // b

print(ans[::-1])