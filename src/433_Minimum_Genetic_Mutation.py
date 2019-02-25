# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       433_Minimum_Genetic_Mutation.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2019-01-29 10:30
@version    0.0.1.20190129
--------------------------------------
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined
    as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank
    to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed
    to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.


Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1


Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
"""


class Solution:
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        
        ## if start gene = end gene, return 0 mutation by default
        if start == end: return 0
        
        ## Create a graph whose nodes are start gene and all elements in bank,
        ## and if a gene node can be transformed to another node by one mutation, then create an edge between them.
        ## Compute the shortest path from start node to end gene node.
        
        ## Create node dictionary, and find the end status.
        
        
        # node_dict = {0: start}
        # start_idx = 0
        # end_idx = -1
        #
        # idx = 0
        # for gene in bank:
        #     if gene not in node_dict.values():
        #         idx += 1
        #         node_dict[idx] = gene
        #
        #     ## find end node
        #     if (end_idx == -1) & (gene == end): end_idx = idx
        #
        # ## if gene end is not in gene bank, we'll never reach this end status, raise error
        # if end_idx == -1: raise ValueError("Parameter Error %s: end gene is not a valid gene string, please check..." % end)
        
        ## Assume there is no duplicate element in bank, and it doesn't contain start node
        node_list = [start] + bank
        start_idx = 0
        nodes_num = len(node_list)

        
        ## Create edge list
        edges = []
        
        end_idx = -1
        for idx, gene in enumerate(node_list):
            if (end_idx == -1) & (gene == end): end_idx = idx
            
            for idx2 in range(idx, nodes_num):
                if self.difference(gene, node_list[idx2]) == 1:
                    edges.append((idx, idx2))

        ## if gene end is not in gene bank, we'll never reach this end status, raise error
        if end_idx == -1: raise ValueError("Parameter Error %s: end gene is not a valid gene string, please check..." % end)
        
        ## find the shortest path from start_idx to end_idx.
        shortest_path = {i: nodes_num+100 for i in range(nodes_num)}
        shortest_path[0] = 0
        connected_part = [0]
        new_connected_part = [0]
        
        while True:
            new_connected_part2 = []
            for new_node in new_connected_part:
                connections = self.conectedNodes(new_node, edges)
                for node1 in connections:
                    if node1 not in connected_part:
                        shortest_path[node1] = shortest_path[new_node]+1
                        new_connected_part2.append(node1)
                        connected_part.append(node1)
                    
                    if node1 == end_idx: return shortest_path[node1]
            
            ## if there is no more new connected node, stop iteration
            if new_connected_part2 == []:
                return -1
                #break
            else:
                new_connected_part = new_connected_part2
            

    def difference(self, gene1, gene2):
        return sum([gene1[i] != gene2[i] for i in range(8)])
        
    def conectedNodes(self, node, edges):
        connections = []
        for edge in edges:
            if edge[0] == node: connections.append(edge[1])
            elif edge[1] == node: connections.append(edge[0])
        
        return connections



if __name__ == "__main__":
    sol = Solution()
    start, end, bank = "AACCGGTT", "AAACGGTA",  ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    
    #print(sol.difference(start,end))
    print(sol.minMutation(start, end, bank))
