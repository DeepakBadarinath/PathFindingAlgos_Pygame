# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:15:13 2020

@author: deepa
"""

import numpy as np

class Edge():
    def __init__(self,start,end,weight=1):
        self.start = start
        self.end = end
        self.weight = weight




def addedge(graph,u,v,weight=1):
    ''' Add directed edge from u to v in graph with weight = 1
    u and v can be tuple/number/string'''
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    
    graph[u].append(Edge(u,v,weight))
    
    return graph


def vertexedges(graph,vertex):
    '''Prints all end point of edges and corr weights protruding out of vertex'''
    print([(edge.end,edge.weight) for edge in graph[vertex]] )


def reverse_edge(edge):
    return Edge(edge.end,edge.start,edge.weight)


graph = {}

addedge(graph,(0,0),(1,0))
addedge(graph,(0,0),(0,1))
addedge(graph,(0,0),(-1,0))
addedge(graph,(0,0),(0,-1))
addedge(graph,(0,1),(0,0))


def create_grid_graph(length=100,width=100):
    graph = {}
    for i in range(length):
        for j in range(width):
            if i>0:
                addedge(graph,(i,j),(i-1,j))
            if i<length-1:
                addedge(graph,(i,j),(i+1,j))
            if j>0:
                addedge(graph,(i,j),(i,j-1))
            if j<width-1:
                addedge(graph,(i,j),(i,j+1))
                
    return graph

#graph = create_grid_graph(500,500)

def pop_edges(graph,node):
    graph[node].clear()


def pop_edge_nbd(graph,node,gridsize,s=3):
    '''destroys a square of length 2s+1 centered at node'''
    for x in range(max(node[0]-s,0),min(node[0]+s,gridsize[0])):
        for y in range(max(node[1]-s,0),min(node[1]+s,gridsize[1])):
            pop_edges(graph,(x,y))
            


def pop_edges_to_vertex(edges,v):
    
    new_edges = [edge for edge in edges if edge.end != v]
    return new_edges

          

def add_to_fringe(graph,v,d,fringe):
    for edge in graph[v]:
        if d[edge.end] == np.inf:
            fringe.append(edge)


def djikstra_edge_select(d,fringe):
    new_edge = fringe[0]
    min_dist = d[new_edge.start] + new_edge.weight
    for edge in fringe:
        if (edge.weight + d[edge.start]) <= min_dist:
            new_edge = edge
            min_dist = d[new_edge.start] + new_edge.weight
        
    return new_edge



def djikstra(graph,start,end=None):
    
    '''Assume start is not end'''
    nodes=graph.keys()
    d={}
    MST = {}
    for node in nodes:
        d[node] = np.inf
        MST[node] = []
        
    d[start] = 0
    fringe = [edge for edge in graph[start]]
    
    while fringe != []:
        
        new_edge = djikstra_edge_select(d,fringe)
        MST[new_edge.start].append(new_edge)
        d[new_edge.end] = d[new_edge.start] + new_edge.weight
        
        fringe = pop_edges_to_vertex(fringe,new_edge.end)
        
        add_to_fringe(graph,new_edge.end,d,fringe)
        
        if new_edge.end == end:
            print("Djikstra found vertex!")
            fringe.clear()
    
    return (MST,d)


#MST_djikstra , d_djikstra = djikstra(graph,(20,20),(100,120))


def manhattan_dist(v,w):
    return (np.abs(v[0]-w[0]) + np.abs(v[1]-w[1]))

 
def a_star_edge_select(d,fringe,end):
    new_edge = fringe[0]
    min_cost = d[new_edge.start] + new_edge.weight + manhattan_dist(new_edge.end,end)
    for edge in fringe:
        if (edge.weight + d[edge.start] + manhattan_dist(edge.end,end)) <= min_cost:
            new_edge = edge
            min_cost = d[new_edge.start] + new_edge.weight + manhattan_dist(new_edge.end,end)
        
    return new_edge


def a_star(graph,start,end):
    nodes=graph.keys()
    d={}
    MST = {}
    for node in nodes:
        d[node] = np.inf
        MST[node] = []
        
    d[start] = 0
    fringe = [edge for edge in graph[start]]
    
    while fringe != []:
        
        new_edge = a_star_edge_select(d,fringe,end)
        MST[new_edge.start].append(new_edge)
        d[new_edge.end] = d[new_edge.start] + new_edge.weight
        
        fringe = pop_edges_to_vertex(fringe,new_edge.end)
        
        add_to_fringe(graph,new_edge.end,d,fringe)
        
        if new_edge.end == end:
            print("A_star found vertex!")
            fringe.clear()
    
    return (MST,d)
    
    
#MST_A_star , d_A_star = a_star(graph,(20,20),(100,120))  



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




