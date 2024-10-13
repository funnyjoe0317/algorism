def char_to_move_count(char):
    return min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)


def solution(name):
    answer = 0
    for i in name:
        # print(i)
        answer += char_to_move_count(i)
    return answer

name = "JEROEN"
# name = "JAN"
print(solution(name))