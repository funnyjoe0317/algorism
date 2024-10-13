import itertools

def solution(k, dungeons):
    answer = 0
    # cnt = 0
    permut = []
    # permut = list(itertools.permutations(dungeons))
    for dungeon in list(itertools.permutations(dungeons)):
        permut.append(list(dungeon))
    # print(permut)
    for dun in permut:
        # print(dun)
        cnt =0
        stair = k
        for item in dun:        
            if stair >= item[0]:
                stair -= item[1]
                # print(stair)
                cnt += 1
        if cnt > answer:
            answer = cnt
    return answer