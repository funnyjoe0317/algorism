def recursion(n, cnt):
    if cnt >=500:
        return -1
    if  n == 1:
        return cnt
    
    if n %2==0:
        n = n // 2
        return recursion(n, cnt+1)
    else:
        n = n*3 +1
        return recursion(n, cnt+1)
    return cnt

def solution(num):
    
    answer = 0
    # print(num)
    answer = recursion(num, answer)
    print(answer)
    return answer

n= 6
solution(n)