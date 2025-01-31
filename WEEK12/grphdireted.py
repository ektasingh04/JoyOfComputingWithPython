#point distribution method
'''
at start all nodes are given equal points
share whatever u hv eqaully with ur neighbors #neighbor vo jisko hm kuch de ske na ki jisse lein(directed graph)
new points of A=sum of old points of some other nodes which give to it 
repeat to many iterations... note that total sum of initial values will be same but individual pts keep changing
at some iteration the pts will saturates or say will be fixed
'''
#create a directed graph

import matplotlib.pyplot as plt
import networkx as nx
import random

def addedge(G):
    nodes=list(G.nodes())
    for s in nodes:     #source and target shld be not same
        for t in nodes:
            if s!=t:
                r=random.random() # we dont want a complete graph so if we get r <0.5 we will add edges else not
                if r<=0.5:
                    G.add_edge(s,t)
    return G

def assignpt(G):
    nodes=list(G.nodes())
    p=[]
    for each in nodes:
        p.append(100) #assign 100 to each
    return p


def distributepoints(G,pts):
    nodes=list(G.nodes())
    newpts=[]
    for i in range(len(nodes)):
        newpts.append(0) # all nodes give to others 
    for n in nodes:
        out=list(G.out_edges(n))
             

def keepdistributing(pts,G):
    nodes=list(G.nodes())
    while 1:
        newpoints=distributepoints(G,pts)
        print(newpoints)
        pts=newpoints
        stop=input("press # to stop or any other key to continue")
        if stop=='#':
            break
    return newpoints



G=nx.DiGraph()
G.add_nodes_from([i for i in range(10)])
G=addedge(G)
nx.draw(G,with_labels=True)
plt.show()

#assign initial points
pts=assignpt(G)
#keep distributing pt
finalpts=keepdistributing(pts,G)