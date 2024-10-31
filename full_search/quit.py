# import sys

# # 입력을 한 번에 받아 각 줄을 처리
# input_data = sys.stdin.read().strip().splitlines()
# n= input_data
# # 각 줄을 [숫자, 숫자] 형태로 변환
# data = [list(map(int, line.split())) for line in input_data]

N = 7
job =[[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]

memo = {}

def sol(day, remain, money):
    if day ==N:
        if remain >0:
            return 0
        return money
    
    # 메모이제이션 : 이미 계산한 값이 있으면 저장된 값 반환
    if (day, remain) in memo:
        return memo[(day, remain)]
    
    # 현재 상담을 하지 않는 경우
    result = sol(day + 1, remain - 1, money)
    
    # 상담을 할 수 있는 경우
    if remain <= 0:
        result = max(result, sol(day + 1, job[day][0]-1, money+job[day][1]))
        
    # 메모이제이션에 저장
    memo[(day, remain)]= result
    return result

print(sol(0,0,0))

# DP테이블 초기화    
dp = [0] * (N+1)

# 뒤에서부터 DP테이블 채우기
for day in range(N-1, -1,-1):
    time, pay = job[day]
    # 상담을 할 수 있는 경우
    if day + time <= N:
        dp[day] = max(dp[day+1], pay+dp[day+time])
    else:
        # 상담을 할 수 없는 경우
        dp[day] = dp[day+1]
        
print(dp[0])