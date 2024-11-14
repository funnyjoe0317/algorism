import sys
# 모든 입력을 한 번에 읽기
# input_data = sys.stdin.read().strip().splitlines()

# 첫 번째 줄: 상근이가 가진 숫자 카드의 개수
# N = int(input_data[0])
N = 10

# 두 번째 줄: 상근이가 가진 숫자 카드 목록 (리스트로 변환)
# sang_cards = list(map(int, input_data[1].split()))
sang_cards = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3,]

# 세 번째 줄: 질문의 개수
# M = int(input_data[2])
M = 8

# 네 번째 줄: 질문 숫자 목록 (리스트로 변환)
# questions = list(map(int, input_data[3].split()))
questions = [10, 9, -5, 2, 3, 4, 5, -10]

nick ={}
for i in sang_cards:
    if i in nick:
        nick[i] +=1
    else:
        nick[i] = 1

# print(nick)
answer = []
for j in questions:
    if j in nick:
        # print(nick[j]   )
        answer.append(nick[j])
    else:
        answer.append(0)
        
print(map(int, answer))