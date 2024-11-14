import itertools

n = 0

_li = []
for i in range(1,n+1):
    _li.append(i)
nPr = itertools.permutations(_li, n)

# print(nPr)
for i in nPr:
    # print(i.join)
    print(" ".join(map(str, i)))

# 그외에
iter = itertools.combinations('1234', 2)
# 12 13 14 23 24 34
for data in iter:
    print(''.join(map(str, data)))
    
iter= itertools.permutations('1234', 2)
# 12 13 14 21 23 24 31 32 34 41 42 43
for data in iter:
    print(*data)
    
iter = itertools.combinations_with_replacement('1234',2)
# 11 12 13 14 22 23 24 33 34 44
for data in iter:
    x,y= data
    print(x,y)
    
iter = itertools.product('1234', repeat=2)
# 11 12 13 14 21 22 23 24 31 32 33 34 41 42 43 44
