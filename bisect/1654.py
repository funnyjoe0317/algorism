# 첫 번째 줄에서 n과 m을 가져오기
lines = input().strip().splitlines()
n, m = map(int, lines[0].split())

# 나머지 숫자들을 리스트로 저장
numbers = list(map(int, lines[1:]))

n =  4
m =  11
numbers =  [802, 743, 457, 539]

start = 1
end = max(numbers)    

while start <= end:
    mid = (start + end)//2
    cnt = 0 
    
    for length in numbers:
        cnt += length // mid
        
    if cnt >=m:
        answer = mid
        start = mid + 1
    else:
        end = mid-1
        
print(answer)
            