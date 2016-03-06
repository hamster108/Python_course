dic = {}
dic2 = {}


def search(a, b):
    if b in dic2[a]:
        ans.append(a)
        return
    for n in dic[a]:
        if b in dic2[n]:
            ans.append(n)
            return
        else:
            return search(n, b)
              
              
n = int(input())
ans = []
for l in range(n):
    st = input().split(' ')
    dic2[st[0]] = []
    h = 0
    if len(st) != 1:
        dic[st[0]] = st[2:]
        while h < len(st[2:]):
            dic2[st[2+h]] = []
            h += 1
    else:
        dic[st[0]] = []    
m = int(input())
for q in range(m):
    new = input().split(' ')
    if new[0] not in dic2:
        dic2[new[0]] = [new[1]]
    else:  
        dic2[new[0]].append(new[1])
z = input().split(' ')
search(z[0], z[1])
if len(ans) != 0:
    for i in ans:
        print(i)
else:
    t = 'None'
    print(t)
