# 해시테이블을 이용해서 조합의 수를 찾아내는 문제
def solution(clothes):
    answer = 1
    hash_table = {}
    
    # print(clothes)
    for item in clothes:
        clothing_item = item[0]
        category = item[1]
        
        if category in hash_table:
            hash_table[category] +=1
        else:
            hash_table[category] = 1
            
    # print(hash_table)
    for cnt in hash_table.values():
        answer *= (cnt +1)
    
    answer -=1
    
    return answer