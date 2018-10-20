from igraph import *
import matplotlib.pyplot as plt
import numpy as np
import powerlaw as pl
import itertools

g = Graph.Read_GML("internet_routers-22july06.gml")

summary(g)

	#Average degree
avg = str((2*g.ecount())/float(g.vcount()))
print("Average degree: " + avg)

	#Average path length
avp = str(g.average_path_length())
print("Average Path length: " + avp)

	#Clustering coefficient
clt = str(g.transitivity_avglocal_undirected())
print("Clustering coefficient: " + clt)

	#Degree distribution
degree=Graph.degree(g)
dist=[]
for x in range(0,max(degree)+1):
	dist.append(degree.count(x)/float(g.vcount()))


	#log
plt.xscale('log')
plt.yscale('log')
plt.xlabel('K')
plt.ylabel('Pk')

plt.plot(dist, linestyle=(0,(1,3)))


results = pl.Fit(degree)
print("Alpha is {}".format(results.power_law.alpha))
print("Xmin is {}".format(results.power_law.xmin))

pl.plot_ccdf(degree, color='r')

plt.show()

print("The network diameter is {}".format(g.diameter()))

print('top betweenness')

	#centrality top10
between = g.betweenness()
between.sort()
print(between[-10:])


print(g.vs.find(_degree=2)["id"])
degree.sort()
maxd = degree[-10:]
vs = VertexSeq(g)

print(maxd)
top=[]
for y in range(len(maxd)):
	top.append(g.vs.select(_degree = maxd[y]))

print()


for x in top:
	a=x.find()
	print(a.betweenness())
