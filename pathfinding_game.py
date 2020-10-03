# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:58:52 2020

@author: deepa
"""

import pygame 
import numpy as np
import shortest_path_algos as sp



def trace_path(tree,node,start,screen,path_color=(240,0,250)):
    while node != start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                node = start
        
        
        l = pygame.draw.line(screen,path_color,node,tree[node][0].end)
        node = tree[node][0].end
        pygame.display.update()
        




pygame.init()

LENGTH = 500
BREADTH  = 500
start = (100,100)
end = (200,152)
screen_size = (LENGTH,BREADTH)


start_color = (0,250,0)
end_color = (250,0,0)
disc_color = (250,250,250)
obs_color = (243,190,49)
path_color = (0,4,250)


goal_radius = 4
disc_radius = 1
obs_len = 15

pygame.display.set_caption("Pathfinding Algos")
screen = pygame.display.set_mode(screen_size)

graph = sp.create_grid_graph(LENGTH,BREADTH)

nodes=graph.keys()
d={}
MST = {}
rev_MST = {}
for node in nodes:
    d[node] = np.inf
    MST[node] = []
    rev_MST[node] = []
    
d[start] = 0
fringe = [edge for edge in graph[start]]

start_point = pygame.draw.circle(screen,start_color,(int(start[0]),int(start[1])),int(goal_radius))
end_point = pygame.draw.circle(screen,end_color,(int(end[0]),int(end[1])),int(goal_radius))
pygame.display.update()




'''

#A* 
while fringe != []:
    
    #pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fringe.clear()

        if pygame.mouse.get_pressed()[0]:
            node = pygame.mouse.get_pos()
            sp.pop_edge_nbd(graph,node,screen_size)
            
            obs = pygame.draw.rect(screen,obs_color,(node[0],node[1],obs_len,obs_len))
            
    new_edge = sp.a_star_edge_select(d,fringe,end)
    MST[new_edge.start].append(new_edge)
    d[new_edge.end] = d[new_edge.start] + new_edge.weight
    
    fringe = sp.pop_edges_to_vertex(fringe,new_edge.end)
    
    sp.add_to_fringe(graph,new_edge.end,d,fringe)
    
    new_point = pygame.draw.circle(screen,disc_color,(int(new_edge.end[0]),int(new_edge.end[1])),int(disc_radius))
    
    rev_MST[new_edge.end].append(sp.reverse_edge(new_edge))

    
    if new_edge.end == end:
        print("A_star found vertex!")
        
        trace_path(rev_MST,new_edge.end,start,screen)
        
        fringe.clear()
    
    pygame.display.update()

pygame.quit()
'''


#Djikstra
while fringe != []:
    
    #pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fringe.clear()
        if pygame.mouse.get_pressed()[0]:
            node = pygame.mouse.get_pos()
            sp.pop_edge_nbd(graph,node,screen_size)
            
            obs = pygame.draw.rect(screen,obs_color,(node[0],node[1],obs_len,obs_len))
        
    new_edge = sp.djikstra_edge_select(d,fringe)
    MST[new_edge.start].append(new_edge)
    d[new_edge.end] = d[new_edge.start] + new_edge.weight
    
    fringe = sp.pop_edges_to_vertex(fringe,new_edge.end)
    
    sp.add_to_fringe(graph,new_edge.end,d,fringe)
    
    new_point = pygame.draw.circle(screen,disc_color,(int(new_edge.end[0]),int(new_edge.end[1])),int(disc_radius))

    rev_MST[new_edge.end].append(sp.reverse_edge(new_edge))
    
    if new_edge.end == end:
        print("Djikstra found vertex!")
        
        trace_path(rev_MST,new_edge.end,start,screen)
        
        fringe.clear()
    
    pygame.display.update()

pygame.quit()




