import sys

# 모든 입력을 한 번에 읽고 줄 단위로 나누기
input_data = sys.stdin.read().strip().splitlines()
# 첫 번째 줄에서 숫자 읽기
n, m = map(int, input_data[0].split())
# 나머지 줄에서 문자열 저장
# n, m = 3,4/
# n_names_list = ['ohhenrie', 'charlie', 'baesangwook']
# n_names_list = input_data[1:3]  
# m_names_list = input_data[1:-1]  
# cnt = 0
# answer = []
# for i in n_names_list:
#     for j in m_names_list:
#         if i ==j:
#             cnt +=1
#             answer.append(i)
# print(cnt)
# # print(answer)
# for i in answer:
#     print(i)

n_names_list = input_data[1:n+1]  
m_names_list = input_data[n+1:n+1+m] 

n_names_list = set(n_names_list)
m_names_list = set(m_names_list)

answer = sorted(n_names_list & m_names_list)

print(len(answer))
for i in answer:
    print(i)