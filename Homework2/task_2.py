n = int(input())
dic = {}
check = []


def search(a):
    if a in check:
        return 
    check.append(a)
    for b in dic[a]:
        if b not in check:
            search(b)


for l in range(n):
    st = input().split(' ')
    if len(st) != 1:
        dic[st[0]] = st[2:]
    else:
        dic[st[0]] = []    
    
m = int(input())
for q in range(m):
    ls = input().split(' ')
    search(ls[1])
    if ls[0] in check:
        print('Yes')
    else:
        print('No')
    check = []
