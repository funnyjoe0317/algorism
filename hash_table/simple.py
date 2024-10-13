    # 해시를 이용해서 풀 수 있는 문제
    # 1. 중복값 찾기
    # 2. 빈도 계산
    # 3. 쌍 찾기
    # 4. 존재 여부 확인
    
def find_duplicates(nums):# 중복값 찾기
    hash_table = {}
    duplicates = []
    
    for num in nums:
        if num in hash_table:
            duplicates.append(num)  # 중복된 숫자를 찾았을 때 리스트에 추가
        else:
            hash_table[num] = True  # 해시 테이블에 숫자 기록
    
    return duplicates

nums = [1, 3, 2, 3, 4, 5, 6, 2]
print(find_duplicates(nums))  # 출력: [3, 2]

# 빈도 계산
def count_frequency(string):
    freq = {}
    
    for char in string:
        if char in freq:
            freq[char] += 1  # 이미 해시 테이블에 있으면 빈도를 증가
        else:
            freq[char] = 1  # 처음 등장한 문자면 1로 초기화
    
    return freq

string = "hello world"
print(count_frequency(string))
# 출력: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# 쌍 찾기
def two_sum(nums, target):
    hash_table = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_table:
            return (hash_table[complement], i)  # 두 수의 인덱스를 반환
        hash_table[num] = i  # 해시 테이블에 현재 숫자의 인덱스를 저장
    
    return None

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # 출력: (0, 1)

