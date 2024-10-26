
import sys 

lines = []
while True:
    try:
        line = input()  # 한 줄씩 입력받기
        if line:  # 비어있지 않은 경우에만 추가
            lines.append(line)
    except EOFError:  # EOF 발생 시 루프 종료
        break

# print(lines)
# n= 11
# m = 5
# lines = ['baekjoononlinejudge', 'startlink', 'codeplus', 'sundaycoding', 'codingsh', 'baekjoon', 'codeplus', 'codeminus', 'startlink', 'starlink', 'sundaycoding', 'codingsh', 'codinghs', 'sondaycoding', 'startrink', 'icerink']

answer = 0
for i, line in enumerate(lines):
    tmp = {'s'}
    
    _set = set(line)
    tmp_num = len(_set)
    _set2 = _set - tmp
    
    if tmp_num == len(_set2):
        continue
    else:
        answer += 1
        if i == m-1:
            break
        
print(answer)
    
import sys

# 첫 번째 줄에서 m과 n 값 받기
m, n = map(int, input().split())

# m과 n이 0인 경우 바로 종료
if m == 0 or n == 0:
    print(0)
else:
    # 이후 n개의 줄을 받는 부분
    lines = []
    for _ in range(n):
        line = input()  # 한 줄씩 입력받기
        lines.append(line)

    # 예시 로직
    answer = 0
    for i, line in enumerate(lines):
        tmp = {'s'}
        
        _set = set(line)
        tmp_num = len(_set)
        _set2 = _set - tmp
        anw = _set - _set2
        if tmp_num == len(_set2):
            continue
        else:
            answer += anw
            if i == m - 1:  # i가 m-1인 경우 루프 종료
                break

    print(answer)



import sys

# 첫 번째 줄에서 m과 n 값 받기
m, n = map(int, input().split())

# m과 n이 0인 경우 바로 종료
if m == 0 or n == 0:
    print(0)
else:
    # 이후 n개의 줄을 받는 부분
    lines = []
    for _ in range(n):
        line = input()  # 한 줄씩 입력받기
        lines.append(line)

    # 예시 로직
    answer = 0
    for i, line in enumerate(lines):
        # 각 라인에서 's'의 개수를 카운트
        s_count = line.count('s')  # 문자열에서 's'의 개수를 셈
        
        # 's'가 하나라도 있으면 answer에 카운트
        answer += s_count
        
        if i == m - 1:  # m번째까지만 처리
            break

    print(answer)

import sys

# 입력을 빠르게 받기
input = sys.stdin.read
data = input().splitlines()

# 첫 번째 줄에서 N과 M을 받음
N, M = map(int, data[0].split())

# 집합 S에 포함된 문자열
S = set(data[1:N+1])

# 검사할 문자열들
check_strings = data[N+1:N+1+M]

# 집합 S에 포함된 문자열의 개수 카운트
answer = sum(1 for s in check_strings if s in S)

# 결과 출력
print(answer)
