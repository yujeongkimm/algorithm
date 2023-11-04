n=int(input())
for _ in range(n):
    h,w,x=map(int,input().split())

    # 나머지는 층
    # [0,H-1]=>[1,H] +1
    floor=(x-1)%h + 1

    # 몫은 호수
    # [1,9]=>0, [1,10]=>1
    # [10,19]=>1 [11,20]=>2
    # [20,29]=>2 [21,30]=>3
    number=(x-1)//h + 1

    print(floor*100+number)