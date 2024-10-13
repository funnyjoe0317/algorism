def build_graph(edges):
    graph = {}
    
    # 간선 리스트를 순회하면서 인접 리스트 방식으로 그래프를 구성
    for u, v in edges:
        if u not in graph:
            graph[u] = []  # u 노드가 그래프에 없으면 빈 리스트로 초기화
        if v not in graph:
            graph[v] = []  # v 노드가 그래프에 없으면 빈 리스트로 초기화
        
        # 양방향 연결을 추가 (u와 v가 서로 연결됨)
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

# 테스트용 간선 리스트
edges = [[1, 2], [1, 3], [2, 4], [3, 5]]

# 그래프 생성
graph = build_graph(edges)

# 생성된 그래프 출력
print(graph)

# {
#     1: [2, 3],
#     2: [1, 4],
#     3: [1, 5],
#     4: [2],
#     5: [3]
# }
