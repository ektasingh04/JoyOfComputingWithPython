#any 2 people in world r related to each other via 6 people in btw them acc to sociology
#connected graph- if atleast one path exists btw any two nodes
#fb network- people r nodes.. edges if 2 people are frnds with eech othr
#edge list reprsentation of graph... #strings in py are immutable

import networkx as nx
import numpy

G=nx.read_edgelist("WEEK9/facebookfile.txt")
#shortest path for each pair of node
N=list(G.nodes()) #list of node of grph

spll=[] #shortest path list

for u in N:
    for v in N:
        if u!=v:
            l=nx.shortest_path_length(G,u,v)  # u and v should not be same node for shortest path they mst be not same
            #shortest psth length in G from source node to destination node weight
            print("shortest path length from ", u, " to ", v," is ",l)
            spll.append(l)
min_spl=min(spll)
max_spl=max(spll) #min max give minm maxm i a lsit
#avg needs numpy
avg_spl=numpy.average(spll)
print("Minimum shortes path length ",min_spl)
print("Maximum shortes path length ",max_spl)
print("average shortes path length ",avg_spl) #avg will be maxm 6 means 6 degrees of sepapartion


