import sys
import heapq
n = int(sys.stdin.readline())

data =[]
heapq.heapify(data)
for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp ==0:
        if not data:
            print('0')
        else:
            print(heapq.heappop(data))
    else:
        heapq.heappush(data, tmp)
    
    
# data = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]

# heapq.heapify(data)

# for i in range(9):
#     tmp = heapq.heappop(data)
#     if tmp == 0:
#         if data:
#             print('0')
#         else:
#             heapq.heappop(data)
#     else:
#         print(heapq.heappop(data))


