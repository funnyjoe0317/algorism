def bin(t):
    tmp = []
    
    
    while t !=1:
        s = t % 2
        # print(s)
        
        # print(t)
        t=t // 2
        tmp.append(int(s))
        if t == 1:
            tmp.append(int(t))
            break
        # print(t)
        # tmp.append(s)
    tmp.sort(reverse=True)
    anw= ''.join(map(str,tmp))
    print(anw)
    return anw

def solution(s):
    answer = []
    # print(bin(4))
    
    cnt_0 = 0
    cnt_2 = 0
    tmp_1 = []
    while True:
        
        for i in s:
            if int(i) == 0:
                cnt_0 +=1
            else:
                tmp_1.append(i)
        print(cnt_0)
        print(tmp_1)
        s = bin(len(tmp_1))
        s = str(s)
        print(s)
        cnt_2 +=1
        print(cnt_2)
        tmp_1 = []
        if not s:
            answer.append(cnt_2,cnt_0)
            break
    
    return answer

solution(s="110010101001")