# def solution(n):
#     answer = 0
#     # 열과 대각선을 기록할 배열 초기화
#     col = [False] * n
#     diag1 = [False] * (2*n-1) # 좌상향 대각선
#     diag2 = [False] * (2*n-1) # 우상향 대각선
#     def place_queen(row):
#         nonlocal answer
#         if row == n:
#             answer += 1
#             return
        
#         for c in range(n):
#             if not col[c] and not diag1[row + c] and not diag2[row - c+n-1]:
#                 # 퀸 배치
#                 col[c] = diag1[row +c] = diag2[row - c +n -1] =True
#                 place_queen(row+1) # 다음 행으로 이동
#                 col[c] = diag1[row +c] = diag2[row -c +n-1] = False
    
#     place_queen(0)                    
#     return answer

def solution(n):
    board = [[0] *n for _ in range(n)] # 체스판을 나타내는 2차원 배열
    answer =0
    
    def is_safe(row, col):
        #세로 체크
        for i in range(row):
            if board[i][col] == 1:
                return False
            
        # left diag
        i, j  = row -1, col -1
        while i >= 0 and j>=0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
            
        # right diag
        i, j= row -1, col +1
        while i >= 0 and j <n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1
            
        return True
    
    def place_queen(row):
        nonlocal answer
        if row == n:
            answer +=1
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                place_queen(row+1)
                board[row][col] = 0
                
    place_queen(0)
    return answer

solution(n=4)