

def solution1(k, room_number):
    answer = []
    
    visited=[False for _ in range(k)]
    position = [0 for _ in range(k)]
    
    for i, k in enumerate(room_number):
        if position[k] ==0:
            position[k] = [room_number[i],i]
        else:
            check = False
            for j in range(1,len(room_number)):
                if position[k+j] == 0 and check == False:
                    position[k+j] = [position[k]+j, i]
                    check =True

    for i in position:
        if i !=0:
            answer.append(i)
        
    return answer

def solution2(k, room_number):
    answer = []
    position = [0] * (k + 1)  # 방 번호에 대한 상태를 저장하는 배열 (0: 빈 방)

    def find_next_available(room):
        # 방이 비어 있으면 그 방을 반환
        if position[room] == 0:
            return room
        # 비어 있지 않으면 다음 빈 방을 재귀적으로 찾아서 반환
        position[room] = find_next_available(position[room])
        return position[room]

    for room in room_number:
        # 예약하려는 방이 비어있는지 확인
        available_room = find_next_available(room)
        answer.append(available_room)
        # 다음으로 가능한 빈 방을 position에 저장
        position[available_room] = available_room + 1

    return answer

def solution(k, room_number):
    room_dic = {}
    ret =[]
    for i in room_number:
        n = i
        visit = [n]
        while n in room_dic:
            n = room_dic[n]
            visit.append(n)
        ret.append(n)
        for j in visit:
            room_dic[j] = n+1
        
    return ret
# 테스트 케이스
# k, room_number = 10, [1, 3, 4, 1, 3, 1]
# print(solution(k, room_number))  # [1, 3, 4, 2, 5, 6]


# [1, 3, 4, 2, 5, 6]
k, room_number = 10, [1, 3, 4, 1, 3, 1]
solution(k, room_number)
