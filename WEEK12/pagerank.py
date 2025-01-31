import networkx as nx
import matplotlib.pyplot as plt
import random

G=nx.gnp_random_graph(7,0.5,directed=True) #we need directed grp to seek importance
nx.draw(G,with_labels=True) #with_labels fn puts labels
plt.show()

#we pick a random  source node x and do a drnkard walk to other node multiple times
x=random.choice([i for i in range(G.number_of_nodes())])
#increment counter of every visited node
dic_coumter={}
for i in range(G.number_of_nodes()): #set all nodes count to 0 frst
    dic_coumter[i]=0

#increment count of source node x
dic_coumter[x]=dic_coumter[x]+1

for i in range(100000):
    listx=list(G.neighbors(x) )     #list to have neighbors
                        #if x is a sink we need to select a node randomly until not sink
                        # otherwise we pick a node from neighbors of x means traverse next to x
    if len(listx)==0:
        x=random.choice([ i for i in range(G.number_of_nodes())])
        dic_coumter[x]=dic_coumter[x]+1
    else:
        x=random.choice(listx)
        dic_coumter[x]=dic_coumter[x]+1

        
''' 
to check if our random method is right or not we have a paerank method in netwokx 
''' 
p=nx.pagerank(G)
print(p)
print(dic_coumter)
'''sorted_p=sorted(p.iems,key=Operator.itemgetter(1))
sorted_dic=sorted(dic_coumter.iems,key=operator.itemgetter(1))
print(sorted_p)
print(sorted_dic)
'''