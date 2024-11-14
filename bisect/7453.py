from itertools import product

A = [-45, -41, -36, -36, 26, -32]
B = [22, -27, 53, 30, -38, -54]
C = [42, 56, -37, -75, 10, 62]
D = [-16, 30, 77, -46, 62, 45]

# A와 B의 모든 합을 구하고 정렬
AB_sums = sorted(a+b for a,b in product(A, B))

CD_sums = [c+d for c, d in product(C,D)]

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left+right) // 2
        if arr[mid] <target:
            left = mid +1
        else:
            right= mid
            
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left <right:
        mid = (left+right)//2
        if arr[mid] <= target:
            left= mid +1
            
        else:
            right =mid
    return left

cnt = 0

for cd_sum in CD_sums:
    target = -cd_sum
    lower = lower_bound(AB_sums, target)
    upper = upper_bound(AB_sums, target)
    cnt += upper - lower
    
print(cnt)