input=input()
stack=[]

for ch in input:
    stack.append(ch)
    
    if stack[-4:]==['P','P','A','P']:
        for _ in range(4):
            stack.pop()
        stack.append('P')
        
if stack==['P'] or stack==['P','P','A','P']:
    print('PPAP')
else:
    print('NP')