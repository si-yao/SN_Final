import networkx as nx
import datetime
from readGraph import Loader
l = Loader()
#this is a file list that the graph built from, now the list only contians 1 file
fileList = ['2013-07 - Citi Bike trip data.csv'];
starttime = datetime.datetime(2013,7,1,0,0,0);
endtime = datetime.datetime(2013,7,2,0,0,0);
#you are loading di-graph with multiple edges, without weight, which is easy to comput degree
G = l.load_MultiDiGraph(starttime, endtime, fileList)
#you also can load as di-graph with weight.
#G = l.load_DiGraph(starttime, endtime, fileList)
print(G.number_of_nodes())