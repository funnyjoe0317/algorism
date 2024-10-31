import heapq

data = [
    [12, 7, 9, 15, 5],
    [13, 8, 11, 19, 6],
    [21, 10, 26, 31, 16],
    [48, 14, 28, 35, 25],
    [52, 20, 32, 41, 49]
]
n = 5
# data =[]
# heapq.heapify(data)
max_heap = []

for i in data:
    for j in i:
        heapq.heappush(max_heap, -j)
        
for i in range(1, n):
    tmp = -heapq.heappop(max_heap)
    if i == n :
        print(tmp)
