def solution(citations):
    # citations을 내림차순으로 정렬
    citations.sort(reverse=True)
    
    # H-Index 계산
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break
            
    return h_index
solution(citations=[3, 0, 6, 1, 5]	)