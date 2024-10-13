def solution(n, times):
    # 이진 탐색 범위 설정
    left = 1
    right = max(times) * n  # 가장 느린 심사관이 모든 사람을 처리하는 경우
    
    answer = right
    
    while left <= right:
        mid = (left + right) // 2  # 중간 시간을 계산
        
        # mid 시간 동안 처리할 수 있는 사람 수 계산 (리스트 컴프리헨션 대신 for 사용)
        total_people = 0
        for time in times:
            total_people += mid // time
        
        if total_people >= n:
            # n명 이상 처리 가능하다면 시간을 더 줄여서 최소 시간 탐색
            answer = mid
            right = mid - 1
        else:
            # n명보다 적게 처리된다면 시간을 늘림
            left = mid + 1
    
    return answer


n = 6 
times = [7, 10]
print(solution(n, times))