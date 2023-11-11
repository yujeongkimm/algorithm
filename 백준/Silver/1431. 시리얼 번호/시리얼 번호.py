# 1. 길이는 짧은 것부터
# 1-1. 길이 같으면, 자릿수 합 작은것 먼저 (숫자만)
# 1-2. 자리수 합 같거나 모두 대문자로 이루어져있다면 알파벳 순으로
class SerialNumber:
    def __init__(self, serial, len, cnt):
        self.serial=serial
        self.len=len
        self.cnt=cnt

def count(serial):
    sum=0
    for s in serial:
        if s.isdigit():
            sum+=int(s)
    return sum

n=int(input())
a=[]
for _ in range(n):
    serial=input()
    a.append(SerialNumber(serial, len(serial), count(serial)))
a.sort(key=lambda x:(x.len, x.cnt, x.serial))

for i in a:
    print(i.serial)



