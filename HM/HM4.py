# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 20:33:17 2018

@author: yinjiang

The file contains the adjacency list representation of a simple undirected graph
There are 200 vertices labeled 1 to 200. The first column in the file represents 
the vertex label, and the particular row (other entries except the first column)
 tells all the vertices that the vertex is adjacent to. 
 So for example, the 6th row looks like : "6	155	56	52	120	......". This just means 
 that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices
 with labels 155,56,52,120,......,etc
Your task is to code up and run the randomized contraction algorithm for the min cut
problem and use it on the above graph to compute the min cut. 

HINT: 
    Note that you'll have to figure out an implementation of edge contractions. 
    Initially, you might want to do this naively, creating a new graph from the 
    old every time there's an edge contraction. But you should also think about
    more efficient implementations 
WARNING:
    please make sure to run the algorithm many times with different random seeds, and
remember the smallest cut that you ever find

"""

# need hashmap for vertices and edges
d = {}
filename = 'kargerMinCut.txt'
totalEdges = 0
with open(filename, 'r') as f:
    for index, item in enumerate(f):
        numbers = [int(number) for number in item.split()]
        d[numbers[0]] = numbers[1:]
        totalEdges += len(numbers[1:]) 
        
def KargerMinCut(d,totalEdges):
    mcut = 0
    while len(d) > 2:
        # keep repeating the following procedures until d only has 2 vertices
        # randomly pick an edge and return related two vertices
        u,v = pick_random_edge(d, totalEdges)
        # i.e. merge v into u
        # total edges reduced depends on # of edges of u and # of edges of v
        totalEdges = totalEdges - v
        totalEdges = totalEdges - u
        # decide to remove v and merge its edges into u
        d[u].extend(d[v])
        # replace v by u for all adjacent edges of v
        for item in d[v]:
            d[item].remove(v)
            d[item].append(u)
        # remove self-loops inside u after merging
        d[u] = list(filter(lambda v: v!=u, d[u]))
        # add new edges to total
        totalEdges = totalEdges + len(d[u])
        # remove v from map
        d.pop(v)
    # now d only have 2 vertices, len(edges) should the same
    for edges in d.values():
        mcut = len(edges)
    return mcut
    
        
    
    
def pick_random_edge(d, totalEdges):
    # d{v: [all adjecent vertices to v] (the length is # of edges to this v)}
    import random
    rand_edge = random.randint(0, totalEdges-1)
    for v,e in d.items():
        if len(e) <= rand_edge:
            rand_edge = rand_edge-len(e)
        else:
            from_v = v
            to_v = e[rand_edge]
            return from_v, to_v

