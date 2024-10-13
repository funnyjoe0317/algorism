# from collections import deque

grid = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 1]
]

# # 초기화
# queue = deque([(0, 0, [])])  # 시작점 (0, 0)
# visited = [[False]*3 for _ in range(3)]
# visited[0][0] = True

# while queue:
#     x, y, path = queue.popleft()
    
#     # 현재 위치와 경로 출력
#     print(f"Popped: {(x, y)}, Path: {path}")
    
#     # 목적지 도달 체크
#     if (x, y) == (2, 2):
#         print(f"Found path: {path + [(x, y)]}")
#         break
    
#     # 상하좌우 이동
#     for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < 3 and 0 <= ny < 3 and grid[nx][ny] == 1 and not visited[nx][ny]:
#             visited[nx][ny] = True
#             queue.append((nx, ny, path + [(x, y)]))


import heapq

# 초기화
pq = [(0, 0, 0, [])]  # (가중치, x, y, 경로)
distance = [[float('inf')]*3 for _ in range(3)]
distance[0][0] = 0

while pq:
    current_weight, x, y, path = heapq.heappop(pq)
    
    # 현재 위치와 경로 출력
    print(f"Popped: {(x, y)}, Current Weight: {current_weight}, Path: {path}")
    
    # 목적지 도달 체크
    if (x, y) == (2, 2):
        print(f"Found path: {path + [(x, y)]}")
        break
    
    # 상하좌우 이동
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3 and grid[nx][ny] == 1:
            new_weight = current_weight + 1
            if new_weight < distance[nx][ny]:
                distance[nx][ny] = new_weight
                heapq.heappush(pq, (new_weight, nx, ny, path + [(x, y)]))
