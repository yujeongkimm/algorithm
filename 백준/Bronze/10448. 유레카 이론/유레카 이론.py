n=int(input())
triangle_list=[] #삼각수 값, 최대값 990, len()최대값 44
a=[0]*1001 # 세 수의 합으로 만들 수 있는 수

for i in range(1,1001):
    num=i*(i+1)//2
    if num>1000:
        break
    triangle_list.append(num)

for i in range(len(triangle_list)):
    for j in range(len(triangle_list)):
        for k in range(len(triangle_list)):
            num=triangle_list[i]+triangle_list[j]+triangle_list[k]
            if num>1000:
                break
            a[num]=1

for _ in range(n):
    k=int(input())
    print(a[k])