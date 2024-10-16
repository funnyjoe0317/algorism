
import sys


n = int(sys.stdin.readline().strip())  # 첫 번째 입력: 배열 크기
target = int(sys.stdin.readline().strip())  # 두 번째 입력: 타겟 숫자

# n = 3
visited = [[False for _ in range(n)] for _ in range(n)]  # 방문 체크 배열
position = [[0 for _ in range(n)] for _ in range(n)]  # 결과를 저장할 배열

# 방향: 아래(↓), 오른쪽(→), 위(↑), 왼쪽(←)
directions = [(1,0), (0,1), (-1,0), (0,-1)]
x, y = 0, 0  # 시작 위치
start_point = n ** 2  # 초기값 (n*n 부터 시작)
# target = 5  # 찾고자 하는 값
dir_idx = 0  # 현재 방향의 인덱스 (처음은 오른쪽)

for _ in range(n*n):
    position[x][y] = start_point
    visited[x][y] = True
    start_point -= 1
    
    if position[x][y] == target:
        anw1, anw2 = x,y
        
    next_x = x+directions[dir_idx][0]
    next_y = y+directions[dir_idx][1]
    
    if not (0<= next_x < n and 0<= next_y<n) or visited[next_x][next_y]:
        dir_idx = (dir_idx+1) % 4
        next_x = x+directions[dir_idx][0]
        next_y = y+directions[dir_idx][1]
    
    x,y = next_x, next_y
    
# 배열 출력: 공백으로 구분된 형태
for row in position:
    print(' '.join(map(str, row)))

    
print(f"{anw1+1} {anw2+1}")