from collections import deque

def make_graph(edges):
    
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

def bfs_deque(road, start, visited):
    queue = deque([start])
    visited[start] = True
    count = 0
    
    while queue:
        node = queue.popleft()
        count +=1
        for neighbor in road[node]:
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return count

def bfs(road, start, visited):
    queue = [start]
    # visited= []
    count = 0
    
    while queue:
        node = queue.pop(0)
        # count +=1
        if node not in visited:
            visited.append(node)
            count +=1
            for neighbor in road[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return count

def cut_node_cnt(road, cut_edge):
    # 자른 간선을 그래프에서 제거
    u, v = cut_edge
    road[u].remove(v)
    road[v].remove(u)
    
    # visited ={}
    visited= []
    count1  = bfs(road, u, visited)
    count2 = bfs(road, v, visited)
    
    return count1-count2

wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
road = make_graph(wires)
# print(road)
cut = [4,7]
print(cut_node_cnt(road, cut))