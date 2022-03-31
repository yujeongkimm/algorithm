s = input()
num = ''
n = 0
for x in s:
    if x.isnumeric():
        if x=='0' and num == '':
            continue
        else:
            num += x
for i in range(1, int(num)+1):
    if int(num)%i == 0:
        n += 1
print(n)