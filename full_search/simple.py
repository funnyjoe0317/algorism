def two_sum_bruteforce(nums, target):
    # 완전 탐색: 모든 경우의 수를 시도
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)  # 합이 target인 두 수의 인덱스 반환
    return None

nums = [2, 7, 11, 15]
target = 9
print(two_sum_bruteforce(nums, target))  # 출력: (0, 1)


from itertools import permutations
# 순열을 이용
def find_permutations(elements):
    perms = permutations(elements)
    for perm in perms:
        print(perm)

elements = [1, 2, 3]
find_permutations(elements)
# 결과
# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)

from itertools import combinations
# 조합 문제
def find_combinations(elements, r):
    combs = combinations(elements, r)
    for comb in combs:
        print(comb)

elements = [1, 2, 3]
find_combinations(elements, 2)

# 결과
# (1, 2)
# (1, 3)
# (2, 3)

# 재귀를 이용한 완전 탐색
def subset(nums, idx=0, current=[]):
    if idx == len(nums):
        print(current)  # 부분 집합 출력
        return
    # 현재 요소를 포함하지 않는 경우
    subset(nums, idx + 1, current)
    # 현재 요소를 포함하는 경우
    subset(nums, idx + 1, current + [nums[idx]])

nums = [1, 2, 3]
subset(nums)
[]
[3]
[2]
[2, 3]
[1]
[1, 3]
[1, 2]
[1, 2, 3]
