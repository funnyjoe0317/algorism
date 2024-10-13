def solution(answers):
    answer = []
    # 1번 찍는 방향  12345 5 
    # 2번 21232425 21232425 8
    # 3번 3311224455 3311224455 10
    # 입력값을 하나씩 맞추어 본다 
    # print(answers)
    cnt_1 = 0
    cnt_1_li = [1,2,3,4,5]
    cnt_2 = 0
    cnt_2_li = [2,1,2,3,2,4,2,5]
    cnt_3 = 0
    cnt_3_li = [3,3,1,1,2,2,4,4,5,5]

    for i, num in enumerate(answers):
        # print(i)
        # print(num)
        if num == cnt_1_li[i % len(cnt_1_li)]:
            cnt_1 += 1
        if num == cnt_2_li[i % len(cnt_2_li)]:
            cnt_2 += 1
        if num == cnt_3_li[i % len(cnt_3_li)]:
            cnt_3 += 1

    rank = [cnt_1, cnt_2, cnt_3]
    # print(f"cnt_1 : {cnt_1}")
    # print(f"cnt_2 : {cnt_2}")
    # print(f"cnt_3 : {cnt_3}")
    idx_rank = []
    for i, value in enumerate(rank):
        idx_rank.append(( value, i+1))
    # print(idx_rank)
    idx_rank.sort(reverse=True, key=lambda x:x[0])
    # print(idx_rank)
    max=idx_rank[0][0]
    for item in idx_rank:
        if item[0] == max:
            answer.append(item[1])
            
    return answer