import sys

# 첫 번째 줄: 멜로디에 포함된 음의 수 N과 한 줄에 있는 프렛의 수 P 입력
# N, P = map(int, sys.stdin.readline().split())

# # 각 음의 줄 번호와 프렛 번호를 저장할 리스트
# melody = []

# # N개의 음을 입력받아서 리스트에 저장
# for _ in range(N):
#     line, fret = map(int, sys.stdin.readline().split())
#     melody.append((line, fret))

# melody 리스트에 모든 음이 (줄 번호, 프렛 번호)로 저장됨
# 5 15
# 2 8
# 2 10
# 2 12
# 2 10
# 2 5

N, P  = 7, 15
melody = [(1, 5), (2, 3), (2, 5), (2, 7), (2, 4), (1, 5), (1, 3)]
cnt = 0
dic = {}
# for i in range(N-1):
#     if melody[i][0] not in dic:
#         dic[melody[i][0]] = []

#     while dic[melody[i][0]] and dic[melody[i][-1]] > melody[i][1]:
#         dic[melody[i][0]].pop()
#         cnt+= 1
        
#     if not dic[melody[i][0]] or dic[melody[i][0]] != melody[i][1]:
#         dic[melody[i][0]].append(melody[i][1])
#         cnt+= 1
# print(cnt)

for line, fret in melody:
    if line not in dic:
        dic[line] = []
        
    while dic[line] and dic[line][-1] > fret:
        dic[line].pop()
        cnt += 1
        
    if not dic[line] or dic[line][-1] != fret:
        dic[line].append(fret)
        cnt+=1

print(cnt)
    
    
        
    


