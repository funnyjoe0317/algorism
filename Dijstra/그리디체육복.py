

def solution(n, lost, reserve):
    answer = n
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    for item in sorted(reserve):
        if item-1 in set_lost:
            set_lost.remove(item-1)
        elif item+1 in set_lost:
            set_lost.remove(item+1)
    
    return answer - len(set_lost)

n=	6
lost = 	[3,5]
reserve = [1, 4]
print(solution(n,lost, reserve))