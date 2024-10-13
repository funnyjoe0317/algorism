# def solution(priorities, location):
#     answer = 0
    
    
#     que =[]
#     for i in range(len(priorities)):
#         que.append((priorities[i], i))
#     print(que)
    
#     que.sort(reverse=True)
#     print(que)
#     for i in range(len(que)):
#         answer +=1
#         if que[i][1] == location:
#             return answer
#     return answer
def solution(priorities, location):
    answer = 0
    que =[]
    end = False
    for i in range(len(priorities)):
        que.append((priorities[i], i))
        
    while que:
        current_set = que.pop(0)
        
        for i in range(len(que)):
            if current_set[0] < que[i][0]:
                que.append(current_set)
                break
            
            if i == len(que)-1:
                end = True
        
        # que.append(current_set)
        
        if end == True:
            answer += 1
            large, loc = current_set
            if loc == location:
                return answer
            
def solution(priorities, location): # 최종
    answer = 0
    que =[]
    end = False
    for i in range(len(priorities)):
        que.append((priorities[i], i))
        
    while que:
        current_set = que.pop(0)
        end = False
        for i in range(len(que)):
            if current_set[0] < que[i][0]:
                end = True
                break
            
        if end:
            que.append(current_set)
        
        # que.append(current_set)
        
        else:
            answer += 1
            large, loc = current_set
            if loc == location:
                return answer



priorities=[2, 1, 3, 2]
location=2
print(solution(priorities, location))