# string = 'baekjoon online judge'
# string =  '<open>tag<close>'
# string = '<   space   >space space space<    spa   c e>'

import sys

# 문자열 입력 받기 (sys.stdin.readline 사용)
string = sys.stdin.readline().strip()
answer = []
str_stack = []
stack = []
for s in string:
    stack.append(s)
    
tmp1 = False
tmp1_stack= []

while stack:
    cur = stack.pop(0)
    if cur == '<' or tmp1 == True or cur == '>':
        if str_stack:
            while str_stack:
                answer.append(str_stack.pop())
            

        tmp1_stack.append(cur)
        tmp1 = True
        if cur == '>':
            for s in tmp1_stack:
                answer.append(s)
            tmp1 = False
            tmp1_stack = []    
    
    if tmp1 ==False:
        if cur == ' ':
            while str_stack:
                answer.append(str_stack.pop())
            answer.append(cur)
        elif cur =='>':
            pass
        else:
            str_stack.append(cur)
            
            
if str_stack:
    while str_stack:
        tmp = str_stack.pop()
        if tmp == ' ':
            break
        answer.append(tmp)
        
# print(answer)
result = ''.join(answer)
print(result)
        
    