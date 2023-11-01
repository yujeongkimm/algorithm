#from itertools import combinations

# 1. 순회하면서 2개빼기
a=[]
for _ in range(9):
    a.append(int(input()))
new_list=[]
rst=sum(a)

# 2. 2개 값 빼면 100 되는지 저장 (i,j)
for i in range(9):
    find=False
    for j in range(i+1,9):
        if rst-a[i]-a[j]==100:
            find=True
            for k in range(9):
                if k!=i and k!=j:
                    new_list.append(a[k])
            break # 찾으면 반복문 빠지기
    if find:
        break

new_list.sort()
for x in new_list:
    print(x)

# for com in combinations(a,7):
#     if sum(com)==100:
#         for i in sorted(com):
#             print(i)
#         break