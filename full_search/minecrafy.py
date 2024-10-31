import sys

# 모든 입력을 한 번에 읽고 줄 단위로 분리
input_data = sys.stdin.read().strip().splitlines()

# 첫 줄에서 3개의 정수를 읽음
first_line = list(map(int, input_data[0].split()))
rows, cols, some_value = first_line[0], first_line[1], first_line[2]

# 2차원 배열 읽기
matrix = [list(map(int, line.split())) for line in input_data[1:]]
import copy
N,M,B = 3,4,99

map_=[
    [5,5,5,5],
    [5,5,5,5],
    [5,5,5,3] 
]
min_height = min(min(row) for row in map_)
max_height = max(max(row) for row in map_)

min_time = float('inf')
best_height = -1


for i in range(min_height, max_height+1):
    B = some_value
    tmp=0 # 
    block_needed = 0 # 목표 높이까지 블록을 쌓는데 필요한 블록 수
    block_removed = 0 # 목표 높이까지 블록을 제거하는데 필요한 블록 수 
    for x,j in enumerate(map_):
        for y,height in enumerate(j):
            if height > i: # 땅파기
                block_removed += (height - i)
                tmp += (height - i) * 2
            elif height < i: # 땅 넣기
                block_needed += (i - height)
                tmp += (i - height) * 1
                
    # 인벤토리에 있는 블록 수와 비교하여 작업 가능한지 확인
    if block_needed <= block_removed + B:
        # 최소 시간 갱신 및 최적 높이 선택
        if tmp < min_time:
            min_time = tmp
            best_height = i
        elif tmp == min_time and i> best_height:
            best_height = i
        
print(best_height, min_time)
