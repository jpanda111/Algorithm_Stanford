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
# karger's algorithm to find minimum cut in an undirected, unweighed and connected graph
from random import randint

class KargerMinCut(object):
    def __init__(self, filename):
        # translate file into hashmap for vertice : all its adjacent vertices
        self.graph = {}
        self.total_edges = 0
        self.filename = filename
        with open(self.filename, 'r') as f:
            for index, line in enumerate(f):
                numbers = [int(number) for number in line.split()]
                self.graph[numbers[0]] = numbers[1:]
                self.total_edges = self.total_edges + len(numbers[1:])
    
    def pick_random_edge(self):
        redge = randint(0, self.total_edges-1)
        # find the corrsponding two vertices and return them
        for v,e in self.graph.items():
            if len(e) <= redge:
                redge = redge - len(e)
            else:
                from_v = v
                to_v = e[redge]
                return from_v, to_v
    
    def minCut(self):
        mCut = 0
        # keep repeating the following procedures until d only has 2 vertices
        while len(self.graph) > 2:
            # randomly pick an edge and return related two vertices
            from_v, to_v = self.pick_random_edge()
            # remove total edges from these two vertices
            self.total_edges -= len(self.graph[from_v])
            self.total_edges -= len(self.graph[to_v])
            # merge to_v into from_v by adding all adjacent edges of to_v first
            self.graph[from_v].extend(self.graph[to_v])
            # replace to_v by from_v for all adjacent edges of to_v
            for item in self.graph[to_v]:
                self.graph[item].remove(to_v)
                self.graph[item].append(from_v)
            # remove self-loops inside from_v map
            self.graph[from_v] = list(filter(lambda x: x!= from_v, self.graph[from_v]))
            # add from_v new total edges back into totaledges
            self.total_edges += len(self.graph[from_v])
            # officially remove to_v from hashmap
            self.graph.pop(to_v)
        # now d only have 2 vertices, len(edges) should the same
        for edges in self.graph.values():
            mCut = len(edges)
        return mCut
    
if __name__=="__main__":
    mCut = 99999
    filename = 'kargerMinCut.txt'
    for i in range(40000): #n=200, times = n^2 = 40000
        kargerMinCutter = KargerMinCut(filename)
        cut = kargerMinCutter.minCut()
        if cut < mCut:
            mCut = cut
        print mCut


a = KargerMinCut(filename)
print a.minCut()