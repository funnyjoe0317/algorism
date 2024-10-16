import sys


# 입력 받기 (z, o와 zoac이 각각 다른 줄에 입력된다고 가정)
input_data = sys.stdin.read().split()  # 공백 기준으로 입력을 나누기

# 첫 번째와 두 번째 문자를 변수로 저장 (소문자로)
start_char1 = input_data[0].lower()  # 'z'
start_char2 = input_data[1].lower()  # 'o'

# 나머지 문자열 저장 (zoac)
target_string = input_data[2]  #
left, right = 'z', 'o'
string = 'zoac'


keybroad_left = [['q','w','e','r','t'],
                 ['a','s','d','f','g'],
                 ['z','x','c','v'] ]
keybroad_right = [['y', 'u','i','o','p'],
                  ['h','j','k','l'],
                  ['b','n','m'] ]

for i in range(len(keybroad_left)):
    for j in range(len(keybroad_left[i])):
        if left == keybroad_left[i][j]:
            current_left=[i, j]
    
for i in range(len(keybroad_right)):
    for j in range(len(keybroad_right[i])):
        if right == keybroad_right[i][j]:
            current_right=[i, j]
            
print(current_left, current_right)
answer  =0

for str in string:
    found = False
    # if str in keybroad_right:
    for i in range(len(keybroad_right)):
        for j in range(len(keybroad_right[i])):
            if str == keybroad_right[i][j]:
                answer += abs(current_right[0] - i)
                answer += abs(current_right[1] -j)
                answer += 1
                current_right=[i, j]
                found = True
                break
    if not found:
        for i in range(len(keybroad_left)):
            for j in range(len(keybroad_left[i])):
                if str == keybroad_left[i][j]:
                    answer += abs(current_left[0] - i)
                    answer += abs(current_left[1] -j)
                    answer += 1
                    current_left = [i, j]
                    break

print(answer)