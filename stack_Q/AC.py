from collections import deque
data = [
    '4',            # 테스트 케이스 수
    'RDD',          # 첫 번째 테스트 케이스의 명령어
    '4',            # 첫 번째 테스트 케이스 배열의 크기
    '[1,2,3,4]',    # 첫 번째 테스트 케이스 배열
    'DD',           # 두 번째 테스트 케이스의 명령어
    '1',            # 두 번째 테스트 케이스 배열의 크기
    '[42]',         # 두 번째 테스트 케이스 배열
    'RRD',          # 세 번째 테스트 케이스의 명령어
    '6',            # 세 번째 테스트 케이스 배열의 크기
    '[1,1,2,3,5,8]', # 세 번째 테스트 케이스 배열
    'D',            # 네 번째 테스트 케이스의 명령어
    '0',            # 네 번째 테스트 케이스 배열의 크기 (빈 배열)
    '[]'            # 네 번째 테스트 케이스 배열 (빈 배열)
]

# import sys
# from collections import deque

# input = sys.stdin.read
# data = input().splitlines()

t = int(data[0])  # 테스트 케이스 수
index = 1

for _ in range(t):
    # 각 테스트 케이스 처리
    commands = data[index]  # 명령어
    n = int(data[index + 1])  # 배열의 크기
    arr = data[index + 2]  # 배열 내용
    
index = 1

for _ in range(t):
    command = data[index]
    n = int(data[index+1])
    arr = data[index+2]
    if arr == '[]':
        st = deque()
    else:
        st = deque(map(int, data[index+2][1:-1].split(',')))
    # print(stack)
    
    reverse = False
    error = False
    for j in command:
        
        if j == 'R':
            reverse = not reverse
        else:
            if not st:
                error = True
                break
            else:
                if reverse:
                    st.pop()
                else:
                    st.popleft()
    if error:
        print('error')
    else:
        if reverse:
            st.reverse()
        print(f"[{','.join(map(str, st))}]")
    index +=3
    
    

