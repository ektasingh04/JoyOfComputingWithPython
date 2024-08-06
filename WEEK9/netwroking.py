#complete graph- pick any 2 nodes there must be an edge btw them
#note===== index(element,beg,end)=> index of 1st occurence of element after beg and before end

import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph() #graph name g empty graph
'''
#adding node
G.add_node(1)
G.add_node(2)
G.add_node(3)   '''

#better method
l=[1,2,3]
G.add_nodes_from(l)

G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,1)

print(G.nodes(),G.edges())
'''nx.draw(G)
plt.show()

#if u want a complete graph
gr=nx.complete_graph(10)
nx.draw(gr)
plt.show()

#random graph
nx.draw(nx.gnp_random_graph(10,0.5)) #degree of each node almost eq to degree of graph .. probability basis
plt.show()

#scale free graph by barabasi ---preferential attachment of new nodes to already higher degree nodes
n=20
m=2
p=nx.barabasi_albert_graph(n,m) #let starting 2 nodes at each new itrn a new node comes with 2 edges   and these 2 edges 
                                #connect to nodes ofhigher degree nodes means km degree ki bhot sari nodes or jyada degree ki bhot km
nx.draw(p)
plt.show()

#save graph as gexf file so that we can import it to gephi
nx.write_gexf(G,'WEEK9/graph1.gexf')
#download gephi ,,open the gexf graph created .. u can take control of a node move it and see how many it is related to
#u can change the color of nodes acc to degree(ranking ),size on basis of rankings degree
# arrange nodes in circular manner..average degree- degree distribuion (power law )
# can impoert in form of comma separated file csv.. as pdf ans many more'''