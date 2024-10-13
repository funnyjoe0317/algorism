import math

def solution(brown, yellow):
    # 전체 타일의 수
    total_tiles = brown + yellow
    
    # 가로, 세로 조합을 찾기 위한 탐색
    for height in range(1, int(math.sqrt(total_tiles)) + 1): # 이거랑 
        if total_tiles % height == 0:  # 나누어 떨어지는 높이를 찾음
            width = total_tiles // height  # 가로 길이 계산
            
            # 갈색과 노란색 타일의 개수가 맞는지 확인
            if (width - 2) * (height - 2) == yellow: # 이게 이 문제 포인트 
                return [width, height]  # 조건을 만족하면 가로, 세로 반환

# 예시 실행
print(solution(10, 2))  # [4, 3]
print(solution(24, 24))  # [8, 6]
