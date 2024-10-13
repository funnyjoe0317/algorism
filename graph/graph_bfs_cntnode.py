def graph(edge):
    _graph ={}
    
    
    for u, v in edge:
        if u not in _graph:
            _graph[u] = []
        if v not in _graph:
            _graph[v] = []
        
        _graph[u].append(v)
        _graph[v].append(u)
    
    return _graph

def bfs(new_graph, start, n):
    visited = [-1] * (n+1)
    visited[start] = 0
    que =[[start, 0]]
    
    while que:
        current = que.pop(0)
        cur_node, cur_distance=current
        for neighbor in new_graph[cur_node]:
            if visited[neighbor] == -1:
                que.append([neighbor, cur_distance+1])
                visited[neighbor] += cur_distance + 1
                
    return visited
                
        
        
        

def solution(n, edge):
    
    start = 1
    new_graph = graph(edge)
    dis = bfs(new_graph, start, n)
    max_dis = max(dis)
    answer = dis.count(max_dis)
    return answer



n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, edge))