stones = 	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3


jump = False
jump_st = 0
sto = 0
# while True:
    
#     for i in range(len(stones)):
#         if stones[i] != 0:
#             stones[i] -=1
#             jump = False
#             jump_st = 0
#         else:
#             if jump == True and jump_st < m-1:
#                 jump_st +=1
#             elif jump_st == m-1:
#                 print(sto)
#                 exit()
#             else:
#                 jump = True
#                 jump_st +=1
#     jump_st = 0
#     jump = False
#     sto += 1

start =1
end = max(stones)

while start <= end:
    mid = (start+end) // 2
    jump_st = 0
    can_cross = True
    
    for stone in stones:
        if stone - mid <= 0:
            # stones[i] -=1
            jump_st += 1
            if jump_st >k:
                can_cross = False
                break
        else:
            jump_st = 0
    
    if can_cross:
        answer =mid
        start = mid+1
    else:
        end = mid- 1
    
print(answer)
