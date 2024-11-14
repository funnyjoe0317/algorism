_list = [4,2,1,3,1]
sorted_list = sorted(_list)
# 오름 차순으로 결과를 리턴
print(' '.join(map(str, sorted_list)))

_list.sort()
# 리스트 메소드로 다른 자료형에서는 사용불가
print(' '.join(map(str, sorted_list)))

wanna_to_eat = [
    ('Chicken', 17900, 'Puradak'),
    ('Pizza', 21000, 'Domino'),
    ('Spagetti', 12000, 'Mola')
]

wanna_to_eat = sorted(wanna_to_eat, key = lambda x:x[1])
print(wanna_to_eat)
wanna_to_eat = sorted(wanna_to_eat, key=lambda x:x[1], reverse =True)
print(wanna_to_eat)

_list1 = [21,61,4,31,65,98]
_list2 = [66,12,34,58,91,3]
_dict = dict(zip(_list1, _list2))
sorted_dict = sorted(_dict.items())

for key, item in sorted_dict:
    print("dictionary[{}] = {}".format(key, item))