import networkx as nx
import numpy

G=nx.read_edgelist("D:\\coding\\python\\Joy of computing using python\\Week 9\\facebook_combined.txt\\facebook_combined.txt")
N=list(G.nodes())

spll=[]

for u in N:
    for v in N:
        if u!=v:
            l=nx.shortest_path_length(G,u,v)
            print("Shortest path between ",u," and ",v," is of length ",l)
            spll.append(l)

min_spll=min(spll)
max_spll=max(spll)
avg_spll=numpy.average(spll)

print("Minimum shortest path length: ",min_spll)
print("Maximum shortest path length: ",max_spll)
print("Average shortest path length: ",avg_spll)