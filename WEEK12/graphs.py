import networkx as nx
import matplotlib.pyplot as plt

U=nx.Graph()
nx.draw(nx.cycle_graph(4))
print(nx.cycle_graph(4).degree)
plt.show()
nx.draw(nx.complete_graph(4))
print(nx.complete_graph(4).degree) # each node connected to rest of all nodes
plt.show()

'''
G=nx.barbell_graph(4,3) #2 clusters of 4 4 nodes are joined by 3 nodes
nx.draw(G)
plt.show()
nx.draw(nx.ladder_graph(5))
plt.show()
nx.draw(nx.cycle_graph(5))
plt.show()
nx.draw(nx.complete_graph(4)) # each node connected to rest of all nodes
plt.show()
nx.draw(nx.path_graph(7))
plt.show()
nx.draw(nx.star_graph(7))  #7 nodes are sink nodes which surround 1 hub node means total n+1 nodes
plt.show()
nx.draw(nx.wheel_graph(7))  
plt.show()

nx.draw(nx.gnp_random_graph(7,0.5))  #7 nodes are sink nodes which surround 1 hub node means total n+1 nodes
plt.show()


dg=nx.DiGraph() #directed graph obj created
dg.add_nodes_from([ i for i in range(5)])
dg.add_edge(1,2)  #from u to v node
dg.add_edge(0,2)
dg.add_edge(2,3)
dg.add_edge(1,3)
dg.add_edge(4,1)

print(list(dg.nodes()))
#in directed graph edges will give only outer edges
e=list(dg.edges())
oe=list(dg.out_edges(2))
ie=list(dg.in_edges(3)) #enter the node u want to find ingoing or outgoing edges of
print(e,oe,ie)
'''
