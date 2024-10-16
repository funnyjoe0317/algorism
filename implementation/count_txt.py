import copy

# n = int(input())  # 예를 들어, 8을 입력

# 그 다음 파일 이름들을 하나씩 입력받습니다
# file_names = [input() for _ in range(n)]
n=8
file_names = ['sbrus.txt', 'spc.spc', 'acm.icpc', 'korea.icpc', 'sample.txt', 'hello.world', 'sogang.spc', 'example.txt']
file_com = False
tmp =[]
answer = []
for s in file_names:
    for ss in s:
        if ss == '.':
            file_com= True
        
        if file_com ==True:
            tmp.append(ss)
    tmp.pop(0)
    file_com=False
    answer.append(''.join(tmp))
    tmp =[]

# print(answer)
# answer.sort()
# print(answer)
# # tmp_list = copy.deepcopy(answer)

# seen = set()
# unique_file_names = []
# for file_name in answer:
#     if file_name not in seen:
#         unique_file_names.append(file_name)
#         seen.add(file_name)
        
# for str in unique_file_names:
#     cur = answer.count(str)
#     print(f"{str} {cur}")
answer.sort()
ext_expan = {}
for sr in answer:
    if sr in ext_expan:
        ext_expan[sr] += 1
    else:
        ext_expan[sr] = 1
        
for ext, count in ext_expan.items():
    print(f"{ext} {count}")