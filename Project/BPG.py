import networkx as nx
import matplotlib.pyplot as plt
import math
class BreakpointGraph:

   def __init__(self):
       self.BPG = nx.MultiGraph()

   def create_BPG(self, genome1, genome2):
       count = 0
       for i in genome1:
           self.BPG.add_edge(i[0], i[1], color = 'red', order = count)
           count += 1
       count = 0
       for j in genome2:
           self.BPG.add_edge(j[0], j[1], color = 'blue', order = count)
           count += 1
       return self.BPG

   def add_edge(self, vertex1, vertex2, color, order):
       self.BPG.add_edge(vertex1, vertex2, color = color, order = order)

   def delete_edge(self, vertex1, vertex2):
       try:
           self.BPG.remove_edge(vertex1, vertex2)
       except:
           raise IndexError('no such edge')

   def pathfinder(self, i):
       # cycle_finder[0] gives the number of pathes
       # cycle_finder[1] gives the number of cycles
       pathes = 0
       cycles = 0
       flag = True
       for j in nx.connected_components(i):
           for vertex in j:
               if nx.degree(i, vertex) == 1:
                   flag = False
           if flag:
               if len(j) != 2: #excluding simple cycles
                   cycles += 1
           else:
               pathes += 1
           flag = True
       return pathes, cycles

   def DCJ_distance(self, i):
       n = len(i.edges())
       c,p = self.pathfinder(i)[1], self.pathfinder(i)[0]
       return float(n - c - p/2)



P = [['Ah','Bt'], ['Ah','Bt'], ['Bh','Ct'], ['Ch','At'], ['Dh','Eh'], ['Et','Ft'], ['Fh','Dt']] #first inputed genome
Q = [['Bt','Ah'], ['Bh','Et'], ['Eh','Fh'], ['Ft','Gt'], ['Ch','Dh'], ['Ct','Dt'], ['Bt','Ah']]
Z = BreakpointGraph().create_BPG(P, Q)
print(Z.edges())
print(Z['Ah'])
print(list(nx.connected_components(Z)))
print(BreakpointGraph().pathfinder(Z))
print(BreakpointGraph().DCJ_distance(Z))

def draw_BPG(graph, first_seq, second_seq, save = False):# option save = True will save our graph as an image
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'), node_color = 'black', node_size=50,
                   alpha=0.8)
    nx.draw_networkx_edges(graph,pos,edgelist= first_seq ,width=2,alpha=0.5,edge_color='r', edge_vmax=100)
    nx.draw_networkx_edges(graph,pos,edgelist= second_seq ,width=2,alpha=0.5,edge_color='b', style = 'dashed')
    if save:
        plt.savefig("breakpoint_graph.png")
    return plt.show()






