
import sys


# 입력 받기 (z, o와 zoac이 각각 다른 줄에 입력된다고 가정)
input_data = sys.stdin.read().split()  # 공백 기준으로 입력을 나누기

# 첫 번째와 두 번째 문자를 변수로 저장 (소문자로)
left = input_data[0].lower()  # 'z'
right = input_data[1].lower()  # 'o'

# 나머지 문자열 저장 (zoac)
string = input_data[2]  #

keyboard_coords = {
    'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4),
    'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8), 'p': (0, 9),
    'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4),
    'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8),
    'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3),
    'b': (2, 4), 'n': (2, 5), 'm': (2, 6)
}

current_left = keyboard_coords[left]
current_right = keyboard_coords[right]

answer = 0

for char in string:
    if char in 'yuiophjklbnm':
        target = keyboard_coords[char]
        answer += abs(current_right[0] - target[0] ) + abs(current_right[1] - target[1]) + 1
        current_right = target
    else:
        target = keyboard_coords[char]
        answer += abs(current_left[0] - target[0]) + abs(current_left[1] - target[1]) + 1
        current_left = target
print(answer)