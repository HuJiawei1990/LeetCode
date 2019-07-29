# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       Graph.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-01-29 13:24
@version    0.0.1.20190129
--------------------------------------
<enter description here>
"""

import sys


class unDirectedGraph(object):
    ## 无序图类别
    def __init__(self, vertices, edges, weights=None):
        """
        :param vertices: List[int]
            List of node's id
        :param edges: List[(int,int)]
            List of edges of the graph. Two nodes are connected if (node1, node2) is in this list.
        :param weights(optional): List[double]
            List of each edge's weight. By default, each weight is set to be 1.
            NOTE:
                - Every weight should be POSITIVE;
                - length of weights' list must EQUAL to length of edges' list.
        """
        self.vertices = [] if vertices is None else vertices
        self.edges = [] if edges is None else edges
        self.weights = [1] * len(edges) if weights is None else weights
    
    
    def NeighboursOfAll(self):
        neighbours = {vertex: [] for vertex in self.vertices}
        
        for e in self.edges:
            neighbours[e[0]].append(e[1])
            neighbours[e[1]].append(e[0])
        
        return neighbours
    
    
    def NeighboursOfVertex(self, vertex):
        neighbours = self.NeighboursOfVertex()
        
        return neighbours[vertex]
    
    
    """
    ### Shortest Path Algorithms  ###
    
    
    """
    
    
    def BFS(self, root):
        """
        
        :param root:
        :return:
        """
        open_nodes = self.vertices
        open_nodes.remove(root)
        closed_nodes = []
        deal_nodes = [root]
        open_edges = self.edges
        
        path = 0
        shortest_path = {root: path}
        while deal_nodes != []:
            path += 1
            deal_nodes_next = []
            print(str(path) + " itetation")
            for edge in open_edges:
                print(edge)
                if (edge[0] in deal_nodes) or (edge[1] in deal_nodes):
                    other_node = edge[1] if edge[0] in deal_nodes else edge[0]
                    if other_node in open_nodes:
                        deal_nodes_next.append(other_node)
                        shortest_path[other_node] = path
                        open_nodes.remove(other_node)
                    
                    # open_edges.remove(edge)
            
            ## refresh deal_nodes & closed_nodes
            closed_nodes += deal_nodes
            deal_nodes = deal_nodes_next
        
        print(shortest_path)
        return shortest_path


if __name__ == "__main__":
    nodes = [0, 1, 2, 3, 4]
    edges = [(0, 1), (0, 2), (1, 3), (3, 4), (2, 3)]
    graph1 = unDirectedGraph(nodes, edges)
    
    graph1.BFS(0)
