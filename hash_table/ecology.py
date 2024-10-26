

tr = [
 'Red Alder', 'Ash', 'Aspen', 'Basswood', 'Ash', 'Beech', 'Yellow Birch', 
 'Ash', 'Cherry', 'Cottonwood', 'Ash', 'Cypress', 'Red Elm', 'Gum', 
 'Hackberry', 'White Oak', 'Hickory', 'Pecan', 'Hard Maple', 'White Oak', 
 'Soft Maple', 'Red Oak', 'Red Oak', 'White Oak', 'Poplan', 'Sassafras', 
 'Sycamore', 'Black Walnut', 'Willow'
]
import sys

# 입력을 빠르게 받기
input = sys.stdin.read

# 여러 줄 입력을 리스트로 변환
tr = input().splitlines()
tr = [t for t in tr if t.strip()]
tr_dict ={}
for t  in tr:
    if t not in tr_dict:
        tr_dict[t] = 1
    else:
        tr_dict[t] += 1
        
# print(tr_dict)
_sum = 0
for name, num  in tr_dict.items():
    _sum += num
    
for name, num in sorted(tr_dict.items()):
    persentage = round((num / _sum) * 100, 4)
    print(f"{name} {tr_dict[name]:.4f}")