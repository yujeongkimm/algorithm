n = int(input())

for i in range(n):
    x = input()
    x = x.upper()
    l = len(x)
    '''
    for k in range(l//2):
        if x[k] != x[l-k-1]:
            print("#%d NO" %(i+1))
            break
    else:
         print("#%d YES" %(i+1))
    '''
    if x==x[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))