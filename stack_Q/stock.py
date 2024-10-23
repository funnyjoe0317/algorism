def solution(prices):
    answer = [0] * len(prices)
    stack =[]
    
    for i in range(len(prices)):
        # 스택이 비어 있지 않고 현재 가격이 스택에 있는 거보다 작을 때
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop() #   이전 인덱스를 가져옴
            answer[j] = i-j 
        stack.append(i) 
        
    while stack:
        j= stack.pop()
        answer[j] =len(prices) -1 -j     
    return answer

solution(prices = [1, 2, 3, 2, 3])