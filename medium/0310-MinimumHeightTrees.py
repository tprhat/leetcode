import collections
from typing import List


# Take out nodes by levels
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj_list = collections.defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        q = []
        degrees = [0] * n
        # Initialize the queue with leaves
        for i in range(n):
            degrees[i] = len(adj_list[i])
            if degrees[i] == 1:
                q.append(i)
                degrees[i] -= 1

        # While there are nodes with degrees > 0
        # Update the degrees of the nodes
        # If a node has degree 1, add it to the queue
        # Repeat until there are no leaves left
        while True:
            ans = q[:]
            q2 = []
            for now in q:
                for v in adj_list[now]:
                    if degrees[v] > 0:
                        degrees[v] -= 1
                        if degrees[v] == 1:
                            q2.append(v)
            if not q2:
                return ans
            q = q2
