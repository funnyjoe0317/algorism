import itertools
import math

def is_prime(n):
    # 1은 소수가 아니므로 False 반환
    if n <= 1:
        return False
    # 2는 소수
    if n == 2:
        return True
    # 짝수는 소수가 아님 (2 제외)
    if n % 2 == 0:
        return False
    
    # 3부터 n의 제곱근까지 홀수만 검사
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    # print(numbers)
    
    char = []
    for item in numbers:
        char.append(item)
        
    permut = []
    
    for r in range(1, len(char)+1): # r은 선택할 숫자의 개수
        perms = list(itertools.permutations(char, r))
        # print(perms)
        for perm in perms:
            permut.append(int(''.join(perm)))
    # print(permut)
    permut = list(set(permut))
    
    permut.sort()
    print(permut)
    
    for item in permut:
        if is_prime(item):
            answer +=1
        
    # print(char)
    return answer