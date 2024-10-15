# 입력값 설정 (테스트용)
n = 3  # 레이어 수

# 정사각형의 크기 계산
size = 4 * n - 3

# 공백(' ')으로 채운 2차원 배열 초기화
grid = [[' ' for _ in range(size)] for _ in range(size)]

# 재귀적으로 테두리를 채우는 함수
def fill_stars_recursive(start, end):
    # 기본 종료 조건: 더 이상 채울 레이어가 없을 때
    if start >= end:
        return

    # 위쪽과 아래쪽 테두리
    for i in range(start, end):
        grid[start][i] = '*'  # 위쪽 테두리
        grid[end - 1][i] = '*'  # 아래쪽 테두리

    # 왼쪽과 오른쪽 테두리
    for i in range(start + 1, end - 1):
        grid[i][start] = '*'  # 왼쪽 테두리
        grid[i][end - 1] = '*'  # 오른쪽 테두리

    # 내부 사각형을 재귀적으로 처리
    fill_stars_recursive(start + 2, end - 2)

# 테두리 그리기 시작
fill_stars_recursive(0, size)

# 결과 출력
output = '\n'.join([''.join(row) for row in grid])
print(output)