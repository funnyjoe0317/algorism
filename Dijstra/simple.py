import heapq

def dijkstra(graph, start):
    
    distances = {node: float('inf') for node in graph}
    
    # 위 식을 풀어서 사용 했을 때
    # distances = {}
    # for node in graph:
    #     distances[node] = float('inf')
    
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        # 우선순위 큐 최단 경로를 찾기 위해 사용되며, heapq모듈은 최소 힙을 사용하여 우선순위 큐를
        # 구현하는 라이브러리. 힙 자료구조는 가장 작은 값이 항상 맨 앞에 오므로 작은 값을 빠르게 꺼냄
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(priority_queue, (distance, adjacent))

    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

distances = dijkstra(graph, 'A')
print(distances)