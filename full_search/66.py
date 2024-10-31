# n = int(input("몇 번째 종말의 수를 찾고 싶으신가요? "))
n = 100
count = 0  # "666"을 포함한 수를 찾은 횟수
number = 666  # 첫 번째 종말의 수는 666부터 시작

# N번째 종말의 수를 찾을 때까지 반복
while True:
    # 현재 숫자에 "666"이 포함되어 있으면
    if "666" in str(number):
        count += 1  # 횟수를 증가
        
        # N번째 종말의 수를 찾았다면 출력하고 종료
        if count == n:
            print(number)
            break
    # 다음 숫자로 증가
    number += 1
