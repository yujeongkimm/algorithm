from collections import Counter
n,c=map(int,input().split())
a=list(map(int,input().split()))
c=Counter(a)
s=sorted(a, key=lambda x: (-c[x],a.index(x)))
print(*s)

# 1. 더 많이 등장한 숫자 먼저
# 2. 등장 횟수 같으면, 입력 들어온 것 먼저
# {num: (count, firstIndex)}
# class Message:
#     def __init__(self, num, idx):
#         self.num=num
#         self.idx=idx
# class Frequency:
#     def __init__(self, num, count, first_idx):
#         self.num=num
#         self.count=count
#         self.first_idx=first_idx
# messages=[]
# frequencies=[]
#
# for i in range(n):
#     messages.append(Message(a[i],i))
#
# messages.sort(key=lambda m:(m.num, m.idx))
#
# frequencies.append(Frequency(messages[0].num, 1, messages[0].idx))
# for i in range(1, n):
#     if messages[i].num != messages[i-1].num:
#         frequencies.append(Frequency(messages[i].num, 0, messages[i].idx))
#     frequencies[-1].count+=1
#
# frequencies.sort(key=lambda f:(-f.count, f.first_idx))
#
# for freq in frequencies:
#     print((str(freq.num)+' ') * freq.count, end='')
