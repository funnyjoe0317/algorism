answer = []
n=2
position = [[0 for _ in range(n) ] for _ in range(n)]
visited = [[False for _ in range(n) ] for _ in range(n)]
direction = [ (1,0), (0,1), (-1,-1)]
dir_point = 1
start = 0
x,y = 0,0
visited[start][start] = True
position[start][start] = 1
while True:
    if n ==1 or n ==2:
        break
        
    # visited[start][start] = True
    # position[start][start] = 1
    for dir in direction:
        while 0 <= x+dir[0] < len(visited) and 0<= y+dir[1] < len(visited):
            if visited[x+dir[0]][y+dir[1]] ==False:
                dir_x ,dir_y = x+dir[0], y+dir[1]
                visited[dir_x][dir_y] = True
                dir_point += 1
                position[dir_x][dir_y] = dir_point
                # print(visited)
                # print(position)
                x, y = dir_x, dir_y
            else:
                if visited[x+1][y] ==True and  visited[x-1][y-1] == True and visited[x][y-1]:
                    break
                else:
                    break
    if visited[x+1][y] ==True and  visited[x-1][y-1] == True and visited[x][y-1]:
        break

if n == 1:
    answer = [1]
elif n ==2:
    answer =[1,2,3]
else:
    for i in range(len(position)):
        for j in range(len(position[i])):
            if position[i][j] != 0:
                answer.append(position[i][j])
                

                