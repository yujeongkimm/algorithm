t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))

    arr.sort()

    _max=0

    for i in range(n-2):
        m=abs(arr[i]-arr[i+2])
        _max=max(m, _max)


    print(_max)