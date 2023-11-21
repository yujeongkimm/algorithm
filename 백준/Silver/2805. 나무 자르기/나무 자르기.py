n,m=map(int,input().split())
trees=list(map(int,input().split()))

def cutTrees(mid):
    cut=0
    for tree in trees:
        if tree>mid:
            cut+=tree-mid
    return cut


l,r=0,max(trees)
res=-1
while l<=r:
    mid=(l+r)//2
    if cutTrees(mid)>=m:
        l=mid+1
        res=mid
    else:
        r=mid-1
print(res)