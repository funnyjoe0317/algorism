# n = int(input())  # 100
n= 100


# 두 번째 줄: 공백으로 구분된 여러 정수를 입력 받아 리스트로 변환
# values = list(map(int, input().split())) 
values= [10, 20, 23, 34, 55, 30, 22, 19, 12, 45, 23, 44, 34, 38]
# values= [20, 20, 33, 98, 15, 6, 4, 1, 1, 1, 2, 3, 6, 14]

# jun,sungmin = n, n
# stock_num =0
# jun_money, sungmin_money = 0, 0
# stock_price =[0 for i in range(len(values))]
# # print(stock_price)
# for i,item in enumerate(values):
#     if i == len(values) - 1:
#         sungmin_money = stock_num * item + sungmin
#         break
    
#     if i != 0 and item < values[i-1]:
#         stock_price[i] = 1
        
#         if sum(stock_price[i-2:i+1])==3 and item <= sungmin:
#             stock_num += sungmin // item
#             sungmin = sungmin % item
#             value = item
            
#     elif i != 0 and item > values[i-1]:
#         stock_price[i] = -1
#         if sum(stock_price[i - 2:i + 1]) == -3:
#             if stock_num != 0:
#                 sungmin_money = stock_num * item
#                 sungmin += sungmin_money
#                 stock_num = 0

#     else:
#         pass
        
# print(sungmin_money)
# jun_stock = 0
# for i in range(len(values)):
#     if i == len(values) -1 :
#         jun_money = jun_stock * values[i] + jun
#         break
    
#     if values[i] <= jun:
#         jun_stock += jun // values[i]
#         jun = jun % values[i]
    
# print(jun_money)
# if jun_money > sungmin_money:
#     print("BNP")
# elif jun_money < sungmin_money:
#     print("TIMING")
# else:
#     print("SAMESAME")

jun, sungmin = n, n
stock_num = 0
jun_money, sungmin_money = 0, 0
stock_price = [0 for i in range(len(values))]

# 성민 전략
for i, item in enumerate(values):
    if i == len(values) - 1:
        sungmin_money = stock_num * item + sungmin
        break

    if i != 0 and item < values[i - 1]:
        stock_price[i] = 1

        if sum(stock_price[i - 2:i + 1]) == 3 and item <= sungmin:
            stock_num += sungmin // item
            sungmin = sungmin % item

    elif i != 0 and item > values[i - 1]:
        stock_price[i] = -1
        if sum(stock_price[i - 2:i + 1]) == -3:
            if stock_num != 0:
                sungmin_money = stock_num * item + sungmin
                stock_num = 0

# 준 전략
jun_stock = 0
for i in range(len(values)):
    if i == len(values) - 1:
        jun_money = jun_stock * values[i] + jun
        break

    if values[i] <= jun:
        jun_stock += jun // values[i]
        jun = jun % values[i]

# 결과 출력
print(sungmin_money)
print(jun_money)

if jun_money > sungmin_money:
    print("BNP")
elif jun_money < sungmin_money:
    print("TIMING")
else:
    print("SAMESAME")
