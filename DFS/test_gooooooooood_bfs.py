def make_graph(wires):
    graph = {}
    for u, v in wires:
        
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
        
    return graph


def cut_edge(wire_graph, cut):
    graph = make_graph(wire_graph)
    u,v = cut[0], cut[1]
    graph[u].remove(v)
    graph[v].remove(u)
    
    visited = []
    
    cnt1 = bfs(graph, u,visited)
    cnt2 = bfs(graph, v,visited)
    
    return abs(cnt1-cnt2)

def bfs(graph,u,visited):
    queue = []
    queue.append(u)
    cnt = 0
    while queue:
        start = queue.pop(0)
        if start not in visited:
            visited.append(start)
            cnt +=1
            for neighbor in graph[start]:
                queue.append(neighbor)
                
    return cnt
                
def solution(n, wires):
    answer = 100000000000000
    # wire_graph = make_graph(wires)
    # print(wire_graph)
    # item= [4,7]
    # print(cut_edge(wire_graph, item))
    for item in wires:
        tmp = cut_edge(wires, item)
        # print(tmp)
        if tmp <= answer:
            answer = tmp
    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))