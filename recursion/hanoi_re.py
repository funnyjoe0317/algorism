def hanoi(n, now, target, mid, answer):
    if n == 1:
        return answer.append([now, target])
    
    hanoi(n-1, now, mid, target, answer)
    answer.append([now, target])
    hanoi(n-1, mid, target, now, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    
    return answer


n=3
print(solution(n))