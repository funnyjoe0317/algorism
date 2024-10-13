def bfs(maps, visited, start):
    que =[[start[0], start[1], 1]]
    visited[0][0] =True
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cnt = 0
    while que:
        current = que.pop(0)
        x,y, dist = current
        if x == len(maps)-1 and y == len(maps[0]) -1:
            return dist
        
        for direction in directions:
            nx, ny = x + direction[0], y +direction[1]
            if 0<= nx < len(maps) and 0 <= ny < len(maps[0]):
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    que.append([nx,ny, dist +1])
                    visited[nx][ny]= True
                    cnt +=1
            
    return -1
            
        
                    
def solution(maps):
    answer = 0
    visited = []
    
    for i in range(len(maps)):
        temp = []
        for j in range(len(maps[i])):
            if maps[i][j] == 1:
                temp.append(False)
            else:
                temp.append(True)
        visited.append(temp)
        
    start = [0,0]
    print(visited)
    answer = bfs(maps,visited, start)
                    
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))