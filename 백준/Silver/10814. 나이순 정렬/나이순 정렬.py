class Member:
    def __init__(self, age:int, name:str, idx:int):
        self.age=age
        self.name=name
        self.idx=idx
    

n=int(input())
members=[]
for i in range(n):
    x,y=input().split()
    x=int(x)
    members.append(Member(x,y,i))

# 1. 나이 증가하는 순 
# 1-1. 나이 같으면 먼저 가입한 순서 -> 인덱스 
members.sort(key=lambda x:(x.age, x.idx))

for member in members:
    print(member.age, member.name)