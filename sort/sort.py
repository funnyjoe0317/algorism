import itertools
def compare(a,b):
    if a+b >b+a:
        return -1
    else:
        return 1


# def solution(numbers): # 상대적으로 느린 방법
#     answer = ''
#     si = list(itertools.permutations(numbers))
#     print(si)
#     max_num = 0
#     for per in si:
#         current = ''.join(map(str, per))
#         print(current)
#         if int(current) >= max_num:
#             max_num = int(current)
#     return max_num

# def solution(numbers):
#     answer = ''
#     print(numbers)
#     sent = list(map(str,numbers))
#     print(sent)
#     max_num = 0
#     for i in range(len(sent)-1):
#         for j in range(i+1, len(sent)):
#             if sent[i] + sent[j] < sent[j] + sent[i]:
#                 sent[i], sent[j] = sent[j], sent[i]
                
#     print(sent)
#     max_num=''.join(sent)
        
#     return max_num

def solution(numbers):
    answer = ''
    # print(numbers)
    sent = list(map(str,numbers))
    # print(sent)
    max_num = 0
    sent.sort(key=lambda x: x*3, reverse=True)
    
    # print(sent)
        
    return max_num

numbers = [6, 10, 2]
print(solution(numbers))