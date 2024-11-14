n, m=3, 7
# _list = []
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         _list.append(i*j)

# _list.sort()
# print(_list[m])

def cnt_less_equal(x,n):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(x//i,n)
        
    return cnt

start, end = 1, n*n
answer =0

while start <= end:
    mid = (start+end) // 2
    if cnt_less_equal(mid, n )>= m:
        answer = mid
        end = mid -1
    else:
        start = mid +1
        
print(answer)