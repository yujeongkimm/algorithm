p=int(input())

for x in range(p):
    a=list(map(int,input().split()))[1:]
    cnt=0
    new_list=[0]*20

    for i in range(20): #a의 요소 20개 순회
        find=False
        for j in range(i):
            # a[i]와 new_list 비교
            if new_list[j]>a[i]:
                # 뒤로 밀림
                for k in range(i,j,-1):
                    new_list[k]=new_list[k-1]
                    cnt+=1
                find=True
                new_list[j]=a[i]
                break
        # a[i]가 가장 크다면
        if not find:
            new_list[i]=a[i]
    print(x+1, cnt)