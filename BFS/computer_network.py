# bfs 풀 떄
# 1. visited를 만든다
# 2. bfs 구현
#    큐에서 시작을 빼
#    while 큐가 사라질때까지
#    
# 3. 탐색할 곳을 지정한다.

def bfs(computers,visited, i):
    visited[i] = True
    que = [i]
    
    while que:
        current = que.pop(0)
        
        for i in range(len(computers)):
            if computers[current][i] == 1 and visited[i] != True:
                que.append(i)
                visited[i] = True
                
    
    return 0


def solution(n, computers):
    visited    =[False] *3
    network = 0
    for i in range(n):
        if not visited[i]:
            bfs(computers, visited, i)
            network +=1
            
    
    # answer = bfs(computers, visited)
    
    return network

computers =[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3

solution(n, computers)