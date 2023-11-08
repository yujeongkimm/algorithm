n=int(input())
a=list(map(int,input().split()))
a_dict={}
a_sort=sorted(a)

rank=0
for i in a_sort:
    if i not in a_dict:
        a_dict[i]=rank
        rank+=1
for i in a:
    print(a_dict[i], end=' ')