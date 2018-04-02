#!/usr/bin/env python3
"""A simple graph class"""

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, node, val):
        if self.graph.get(node, False):
            self.graph[node].append(val)
        else:
            self.graph[node] = [val]

    # Graphs have no root, you can start by whatever node you want
    def dfs(self, node):
        visited = {}
        res = set()
        self._dfs(node, visited, res)
        return res

    def _dfs(self, node, visited, res):
        visited[node] = True
        res.add(node)
        for adjacent in self.graph[node]:
            # if visited[adjacent] == False:
            if not visited.get(adjacent):
                self._dfs(adjacent, visited, res)


g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# =============================================================================

accounts = [["John", "a@mail.com", "b@mail.com"],
            ["John", "c@mail.com"],
            ["John", "a@mail.com", "d@mail.com"],
            ["Mary", "f@mail.com"]]

import collections
from pprint import pprint
def accountsMerge(accounts):
    em_to_name = {}
    graph = collections.defaultdict(set)
    for acc in accounts:
        name, email_list = acc[0], acc[1:]
        for i in email_list:
            graph[email_list[0]].add(i)
            graph[i].add(email_list[0])
            # for j in email_list:
            #     graph[i].add(j)
            em_to_name[i] = name
    pprint(em_to_name)
    pprint(graph)
    return graph, em_to_name


graph, em_to_name = accountsMerge(accounts)

seen = set()
ans = []
for email in graph:
    if email not in seen:
        seen.add(email)
        stack = [email]
        component = []
        while stack:
            node = stack.pop()
            component.append(node)
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)
        ans.append([em_to_name[email]] + sorted(component))


print(ans)