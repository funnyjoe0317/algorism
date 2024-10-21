s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

answer = []
s=s[2:-2].split("},{")
# print(s)
# s=sorted(s,key = lambda x:len(x), reverse=True)
s=sorted(s,key = lambda x:len(x))
# s.sort()
# print(s)
for i in s:
    ii = i.split(',')
    for j in ii:
        if int(j) not in answer:
            # print(j)
            answer.append(int(j))
            # print(answer)