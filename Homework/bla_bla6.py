import networkx as nx
c = 0
n = input()

def search(t):
    for el in list(inh.successors(t)):
        if el == s[1]:
            ans.append('Yes')
            return True
        elif inh.successors(t) == []:
            break
        else:
            search(el)

inh = nx.DiGraph()
while c < n:
    i = raw_input().split(' ')
    inh.add_node(i[0])
    if len(i) != 1:
        k = len(i)
        j = 2
        h = 0
        while j < k:
            inh.add_node(i[2+h])
            inh.add_edge(i[2+h], i[0])
            j += 1
            h += 1
    c += 1

q = input()
f = 0
ans = []
while f < q:
    s = raw_input().split(' ')
    if not search(s[0]):    
        ans.append('No')       
    f += 1
for i in ans:
    print(i)


            
