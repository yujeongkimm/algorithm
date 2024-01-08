s,p=map(int,input().split())
string=input()
a,c,g,t=map(int,input().split())

cnt=0
start=string[:p]
dic={'A':0, 'C':0, 'G':0, 'T':0}
for i in start:
    dic[i]+=1

if dic['A']>=a and dic['C']>=c and dic['G']>=g and dic['T']>=t:
    cnt+=1

for i in range(1, s-p+1):
    dic[string[i-1]]-=1
    dic[string[i+p-1]]+=1
    if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
        cnt += 1
print(cnt)