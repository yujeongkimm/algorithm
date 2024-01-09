t=int(input())
letters=[input() for _ in range(t)]

def is_same(sequence):
    if sequence==sequence[::-1]:
        return True
    return False

for l in letters:
    left,right=0,len(l)-1
    ans=0

    while left<=right:
        if l[left]!=l[right]:
            #회문인지
            if is_same(l[left:right]) or is_same(l[left+1:right+1]):
                ans=1
            else:
                ans=2
            break
        right-=1
        left+=1
    print(ans)