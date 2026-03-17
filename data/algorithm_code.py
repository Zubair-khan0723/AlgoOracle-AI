ALGORITHM_CODE = {

"Sorting":"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
""",

"Backtracking":"""
def permute(nums):
    res=[]

    def backtrack(path):
        if len(path)==len(nums):
            res.append(path[:])
            return

        for n in nums:
            if n in path:
                continue
            path.append(n)
            backtrack(path)
            path.pop()

    backtrack([])
    return res
""",

"Graph Traversal":"""
from collections import deque

def bfs(graph,start):
    visited=set()
    queue=deque([start])

    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
""",

"Shortest Path":"""
import heapq

def dijkstra(graph,start):
    dist={node:float('inf') for node in graph}
    dist[start]=0
    pq=[(0,start)]

    while pq:
        cost,node=heapq.heappop(pq)
        for neighbor,w in graph[node]:
            new=cost+w
            if new<dist[neighbor]:
                dist[neighbor]=new
                heapq.heappush(pq,(new,neighbor))
"""
}