def check(room):
    
    direction = [(-1,0), (1,0), (0,-1), (0,1)]
    manhattan_direction = [(-2,0), (2,0), (0,-2), (0,2)]
    diagonals = [(-1,-1), (-1,1), (1,-1),(1,1)]
    
    rows, cols = len(room),len(room[0])    

    for i in range(rows):
        for j in range(cols):
            if room[i][j] == 'P':
                # 맨해튼 1 검사
                for di, dj in direction:
                    ni,nj = i+di, j+dj
                    if 0<= ni <rows and 0 <=nj <cols and room[ni][nj] =='P':
                        return 0
                for di, dj in manhattan_direction:
                    ni,nj = i+di, j+dj
                    if 0<= ni <rows and 0<=nj <cols and room[ni][nj] == 'P':
                        if di == -2 or di ==2: # 위 아래에  두 칸 떨어진 경우
                            if room[i+di//2][j] != 'X':
                                return 0
                        if dj == -2 or dj ==2:
                            if room[i][j+dj//2] != 'X':
                                return 0 
                
                for di, dj in diagonals:
                    ni,nj =i+di, j+dj
                    if 0<= ni < rows and 0<=nj <cols and room[ni][nj]=='P':
                        if not (room[i+di][j]=='X' and room[i][j+dj]=='X'):
                            return 0
                        
    return 1

def solution(places):
    answer = []
    # print(places)
    for room in places:
        answer.append(check(room))
    return answer