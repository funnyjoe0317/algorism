# N, M = map(int, input().split())  # N과 M을 입력으로 받음
N, M =4, 2
_list = []  # 수열을 저장할 리스트

# def solve(_list, N, M):
#     # 종료 조건: _list가 M개의 숫자를 포함하면 조건에 맞는 수열이 완성된 것이므로 출력
#     if len(_list) == M:
#         print(" ".join(map(str, _list)))
#         return
    
#     # 1부터 N까지의 숫자를 차례로 시도
#     for i in range(1, N + 1):
#         if i not in _list:  # 중복을 방지하기 위한 조건
#             _list.append(i)  # 선택한 숫자 i를 _list에 추가
#             solve()          # 다음 숫자를 선택하기 위해 재귀 호출
#             _list.pop()      # 현재 숫자 i를 제거하고 이전 상태로 돌아감 (백트래킹)

# solve(_list, N, M)

# def solve(sequence):
#     # 종료 조건: sequence의 길이가 M이면 출력하고 종료
#     if len(sequence) == M:
#         print(" ".join(map(str, sequence)))
#         return

    
#     for i in range(1, N + 1):
#         # 중복 방지를 위해 이미 sequence에 포함된 숫자는 제외
#         if i not in sequence:
#             sequence.append(i)  # 현재 숫자 추가
#             solve(sequence)     # 재귀 호출
#             sequence.pop()      # 백트래킹: 추가한 숫자 제거하여 이전 상태로 돌아감

# # 입력 처리
# N, M = map(int, input().split())
# solve([])  # 초기에는 빈 리스트를 전달하여 호출

# N, M = map(int, input("Enter N and M: ").split())

def solve(sequence, start):
    if len(sequence) == M:  # 종료 조건: 길이가 M인 경우
        print(" ".join(map(str, sequence)))  # 수열 출력
        return
    
    for i in range(start, N + 1):  # start부터 N까지 반복
        sequence.append(i)         # 선택한 숫자를 추가
        solve(sequence, i + 1)     # 재귀 호출, 다음 숫자는 i + 1부터 선택
        sequence.pop()             # 백트래킹: 마지막 숫자 제거하여 이전 상태로 돌아감

# 초기 호출 - 빈 리스트와 시작 인덱스 1로 호출
solve([], 1)
