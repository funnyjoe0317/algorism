
def solution(triangle):
    t = []
    
    for i in triangle:
        t.append(i[:])
    
    print(t)
    max_num = 0
    for i in range(1, len(t)):
        for j in range(len(t[i])):
            if j == 0:
                t[i][j] += t[i-1][j]
            elif j ==len(t[i])-1:
                t[i][j] += t[i-1][j-1]
            else:
                t[i][j] +=  max(t[i-1][j-1], t[i-1][j])
        
    # for i in range()
    max_num = max(t[len(t)-1])
    return max_num 



triangle = [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5]
]

print(solution(triangle))  # 결과: 30