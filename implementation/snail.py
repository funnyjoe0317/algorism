n = 3
visited = [[False for i in range(n)]for i in range(n)]
print(visited)

target = 5

direction = [(1,0), (0,1), (-1,0), (0,-1)]
position = [[0 for i in range(n)]for i in range(n)]
print(position)
x, y= 0,0
start_point = n**2
position[x][y] = start_point

while visited:
    
    
    for dir in direction:
        visited[x][y] = True
        # position[x][y] = start_point
        
        cur_x, cur_y = abs(x+dir[0]), abs(y+dir[1])
        while 0 <= cur_x < len(visited) and 0<= cur_y <len(visited):
            if not visited[cur_x][cur_y]:
                
                visited[cur_x][cur_y] = True
                start_point -= 1
                position[cur_x][cur_y] = start_point
                
                if position[cur_x][cur_y] == target:
                    anw1, anw2 = cur_x, cur_y
            if 0<= cur_x+dir[0]<= len(visited) and 0<= cur_y <= len(visited):
                cur_x, cur_y = abs(cur_x+dir[0]), abs(cur_y+dir[1])
            else:
                break
        
        if not 0 <= cur_x < len(visited):
            x,y = cur_x-1, cur_y
        else:
            x,y = cur_x, cur_y-1
        
        
pass