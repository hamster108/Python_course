n = int(input())
dic = {}
passed = []
ancestors = []
noneed = []


def search(a):
    for b in dic[a]:
        if b not in ancestors:
            ancestors.append(b)
            search(b)
   
            
for l in range(n):
    st = input().split(' ')
    if len(st) != 1:
        dic[st[0]] = st[2:]
    else:
        dic[st[0]] = []
m = int(input())
for q in range(m):
    ls = input()
    flag = 0
    search(ls)
    passed.append(ls)
    for h in ancestors:
        for el in passed:
            if h == el:
                flag = 1
    if flag == 1:
        noneed.append(ls)
        flag = 0
    ancestors = []
for k in noneed:
    print(k)
